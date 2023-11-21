from typing import Type, List

import numpy as np


class BaseActivation:
    def forward(self, layer: np.ndarray) -> np.ndarray:
        raise NotImplementedError

    def backward(self, layer: np.ndarray) -> np.ndarray:
        raise NotImplementedError


class LinearActivation(BaseActivation):
    def forward(self, layer: np.ndarray) -> np.ndarray:
        return layer

    def backward(self, layer: np.ndarray) -> np.ndarray:
        return np.ones(layer.shape)


class ReluActivation(BaseActivation):
    def forward(self, layer: np.ndarray) -> np.ndarray:
        return np.maximum(layer, 0)

    def backward(self, layer: np.ndarray) -> np.ndarray:
        return np.where(layer > 0, 1, 0)


class LeakyReluActivation(BaseActivation):
    def __init__(self, coeff=1.0/5.5):
        self.coeff = coeff

    def forward(self, layer: np.ndarray) -> np.ndarray:
        return np.where(layer > 0, layer, layer * self.coeff)

    def backward(self, layer: np.ndarray) -> np.ndarray:
        return np.where(layer > 0, 1, self.coeff)


class SigmoidActivation(BaseActivation):
    def forward(self, layer: np.ndarray) -> np.ndarray:
        return 1.0 / (1.0 + np.exp(-layer))

    def backward(self, layer: np.ndarray) -> np.ndarray:
        f = self.forward(layer)
        return f * (1 - f)


class BaseLossFunction:
    def compute_loss(self, y_true: np.ndarray, y_pred: np.ndarray) -> np.ndarray:
        raise NotImplementedError

    def compute_gradient(self, y_pred: np.ndarray, y_true: np.ndarray) -> np.ndarray:
        raise NotImplementedError


class MeanSquareLoss(BaseLossFunction):
    def compute_loss(self, y_pred: np.ndarray, y_true: np.ndarray) -> np.ndarray:
        return ((y_pred - y_true) ** 2) / 2

    def compute_gradient(self, y_pred: np.ndarray, y_true: np.ndarray) -> np.ndarray:
        return (y_pred - y_true)


class CrossEntropyLoss(BaseLossFunction):
    def __init__(self, epsilon=1e-7):
        self.epsilon = epsilon

    def compute_loss(self, y_true: np.ndarray, y_pred: np.ndarray) -> np.ndarray:
        return -(y_true * np.log(y_pred + self.epsilon) + (1 - y_true) * np.log(1 - y_pred + self.epsilon))

    def compute_gradient(self, y_pred: np.ndarray, y_true: np.ndarray) -> np.ndarray:
        return (y_pred - y_true) / ((1 - y_pred) * y_pred + self.epsilon)


class DenseNeuralNetwork:
    # Split activations to 2 types: intermediate and the very last one
    # It is often preferrable, that intermediate activations are RELU-like activations,
    # whereas last activation is sigmoid-like activation
    activation_klass: Type[BaseActivation] = LeakyReluActivation
    last_activation_klass: Type[BaseActivation] = SigmoidActivation
    loss_function_klass: Type[BaseLossFunction] = CrossEntropyLoss

    def __init__(self, blocks=(), bias=True):
        self.blocks: List[int] = blocks
        self.bias: bool = bias
        self.layers: List[np.ndarray] = self.initialize_layers()
        self.activation_fn: BaseActivation = self.activation_klass()
        self.last_layer_activation_fn: BaseActivation = self.last_activation_klass()
        self.loss_fn: BaseLossFunction = self.loss_function_klass()

    def initialize_layers(self) -> List[np.ndarray]:
        layers = []
        for prev_block, next_block in zip(self.blocks[:-1], self.blocks[1:]):
            # For RELU use normal initialization
            # For Sigmoid (as intermediate) use uniform initialization
            layers.append(
                np.random.normal(
                    size=(prev_block + self.bias, next_block),
                    scale=2/(prev_block + next_block + 1),
                ),
            )
        return layers

    def forward(self, x_data: np.ndarray) -> List[np.ndarray]:
        assert x_data.shape[0] == self.blocks[0]

        nodes = []
        nodes.append(np.copy(x_data))
        node = np.concatenate([x_data] + [np.array([1])] * self.bias, axis=0)

        for layer in self.layers:
            node = np.dot(node, layer)
            nodes.append(np.copy(node))
            node = self.activation_fn.forward(np.concatenate([node] + [np.array([1])] * self.bias, axis=0))

        return nodes

    def backward(self, nodes: List[np.ndarray], labels: np.ndarray, learning_rate=0.001, weight_decay=0.001):
        # Compute gradient of loss over linear combination in last nodes
        y_true = labels
        y_pred = self.last_layer_activation_fn.forward(nodes[-1])
        backprop_gradients = []

        loss_gradient = self.loss_fn.compute_gradient(y_pred=y_pred, y_true=y_true)
        last_nodes_gradient = self.last_layer_activation_fn.backward(nodes[-1]) * loss_gradient

        _pre_last_nodes = np.concatenate(
            [self.activation_fn.forward(nodes[-2])] + [np.array([1.0])] * self.bias,
            axis=0,
        )
        backprop_gradients.append(
            np.expand_dims(_pre_last_nodes, axis=1) *
            np.expand_dims(last_nodes_gradient, axis=0)
        )

        for layer_idx in range(len(self.layers)-1, -1, -1):
            _node = nodes[layer_idx]
            _last_node_gradient = np.zeros(_node.shape)
            _activation_grad = self.activation_fn.backward(_node)
            for j in range(_last_node_gradient.shape[0]):
                s = 0
                for k in range(nodes[layer_idx+1].shape[0]):
                    s += self.layers[layer_idx][j,k] * last_nodes_gradient[k] * _activation_grad[j]
                _last_node_gradient[j] = s
            last_nodes_gradient = _last_node_gradient.copy()

            if layer_idx != 0:
                _pre_last_nodes = np.concatenate(
                    [self.activation_fn.forward(nodes[layer_idx-1])] + [np.array([1.0])] * self.bias,
                    axis=0,
                )
                backprop_gradients.append(
                    np.expand_dims(_pre_last_nodes, axis=1) *
                    np.expand_dims(last_nodes_gradient, axis=0)
                )

        for reverse_layer_idx, grad in enumerate(backprop_gradients):
            idx = len(self.layers) - 1 - reverse_layer_idx
            self.layers[idx] -= learning_rate * grad
            # L2 regularization
            self.layers[idx] -= weight_decay * learning_rate * self.layers[idx]

    def prediction(self, nodes: List[np.ndarray]) -> np.ndarray:
        return self.last_layer_activation_fn.forward(nodes[-1])


class XORDataset:
    def __init__(self):
        self.data = [
            (np.array([0.0, 0.0]), np.array([0.0])),
            (np.array([1.0, 0.0]), np.array([1.0])),
            (np.array([0.0, 1.0]), np.array([1.0])),
            (np.array([1.0, 1.0]), np.array([0.0])),
        ]
        self.cur_idx = 0

    def __iter__(self):
        self.cur_idx = 0
        return self

    def __next__(self):
        if self.cur_idx >= 4:
            raise StopIteration

        val = self.data[self.cur_idx]
        self.cur_idx += 1
        return val

    def __len__(self):
        return 4


if __name__ == "__main__":
    neural_network = DenseNeuralNetwork(blocks=(2, 3, 3, 1), bias=True)
    dataset = XORDataset()
    learning_rate = 0.01

    for epoch in range(5000):
        print("EPOCH: ", epoch)
        total_loss = 0
        for x_data, y_true in dataset:
            nodes = neural_network.forward(x_data)
            y_pred = neural_network.prediction(nodes)
            loss = neural_network.loss_fn.compute_loss(y_pred=y_pred, y_true=y_true)
            total_loss += np.abs(loss).sum()
            neural_network.backward(nodes, y_true, learning_rate=learning_rate)

        print("AVERAGE LOSS", total_loss / len(dataset))

    # Evaluate
    for x_data, y_true in dataset:
        nodes = neural_network.forward(x_data)
        y_pred = neural_network.prediction(nodes)
        print("--------------")
        print("INSTANCE", x_data)
        print("PREDICTED", y_pred)
        print("ACTUAL", y_true)
