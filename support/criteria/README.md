# Criteria

## Mean Squared Error

### Gradient Calculation

<!--
\text{Given labels} y \text{and predictions} \hat{y} \text{, the derivative with respect to }\hat{y}, \frac{\partial{}}{\partial{}\hat{y}}
-->
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Ctext%7BGiven+labels%7D+y+%5Ctext%7Band+predictions%7D+%5Chat%7By%7D+%5Ctext%7B%2C+the+derivative+with+respect+to+%7D%5Chat%7By%7D%2C+%5Cfrac%7B%5Cpartial%7B%7D%7D%7B%5Cpartial%7B%7D%5Chat%7By%7D%7D">

<!--
\begin{align*}
n \in{} \mathbb{R}; \frac{1}{n} \sum^{n}_{i} {\left( y_{i} - \hat{y}_{i} \right)}^{2} & \\
\frac{\partial{}}{\partial{}\hat{y}} \left( \frac{1}{n} \sum^{n}_{i} {\left( y_{i} - \hat{y}_{i} \right)}^{2} \right) &= \frac{1}{n} \sum^{n}_{i} \left( \frac{\partial{}}{\partial{}\hat{y}} {\left( y_{i} - \hat{y}_{i} \right)}^{2} \right) \\
&= \frac{1}{n} \sum_{i}^{n} \left( 2\left( y_{i} - \hat{y}_{i} \right) * \frac{\partial{}}{\partial{}\hat{y}}(y_{i} - \hat{y}_{i}) \right) \\
&= -\frac{1}{n} \sum_{i}^{n} \left( 2\left( y_{i} - \hat{y}_{i} \right) \right) \\
\end{align*}
-->
<img src="https://render.githubusercontent.com/render/math?math=%5Ctextstyle+%5Cbegin%7Balign%2A%7D%0An+%5Cin%7B%7D+%5Cmathbb%7BR%7D%3B+%5Cfrac%7B1%7D%7Bn%7D+%5Csum%5E%7Bn%7D_%7Bi%7D+%7B%5Cleft%28+y_%7Bi%7D+-+%5Chat%7By%7D_%7Bi%7D+%5Cright%29%7D%5E%7B2%7D+%26+%5C%5C%0A%5Cfrac%7B%5Cpartial%7B%7D%7D%7B%5Cpartial%7B%7D%5Chat%7By%7D%7D+%5Cleft%28+%5Cfrac%7B1%7D%7Bn%7D+%5Csum%5E%7Bn%7D_%7Bi%7D+%7B%5Cleft%28+y_%7Bi%7D+-+%5Chat%7By%7D_%7Bi%7D+%5Cright%29%7D%5E%7B2%7D+%5Cright%29+%26%3D+%5Cfrac%7B1%7D%7Bn%7D+%5Csum%5E%7Bn%7D_%7Bi%7D+%5Cleft%28+%5Cfrac%7B%5Cpartial%7B%7D%7D%7B%5Cpartial%7B%7D%5Chat%7By%7D%7D+%7B%5Cleft%28+y_%7Bi%7D+-+%5Chat%7By%7D_%7Bi%7D+%5Cright%29%7D%5E%7B2%7D+%5Cright%29+%5C%5C%0A%26%3D+%5Cfrac%7B1%7D%7Bn%7D+%5Csum_%7Bi%7D%5E%7Bn%7D+%5Cleft%28+2%5Cleft%28+y_%7Bi%7D+-+%5Chat%7By%7D_%7Bi%7D+%5Cright%29+%2A+%5Cfrac%7B%5Cpartial%7B%7D%7D%7B%5Cpartial%7B%7D%5Chat%7By%7D%7D%28y_%7Bi%7D+-+%5Chat%7By%7D_%7Bi%7D%29+%5Cright%29+%5C%5C%0A%26%3D+-%5Cfrac%7B1%7D%7Bn%7D+%5Csum_%7Bi%7D%5E%7Bn%7D+%5Cleft%28+2%5Cleft%28+y_%7Bi%7D+-+%5Chat%7By%7D_%7Bi%7D+%5Cright%29+%5Cright%29+%5C%5C%0A%5Cend%7Balign%2A%7D">

The vectorized equivalent

<!--
\begin{align*}
n \in{} \mathbb{R}, v = y - \hat{y}; \frac{1}{n} vv^{T} & \\
\frac{\partial{}}{\partial{}\hat{y}} \left( \frac{1}{n} vv^{T} \right) &= \frac{1}{n} \left( \frac{\partial{}}{\partial{}\hat{y}} \left( vv^{T} \right) \right) \\
&= -\frac{1}{n} 2v \equiv{} -\frac{1}{n}2(y - \hat{y}) \\
\end{align*}
-->
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0An+%5Cin%7B%7D+%5Cmathbb%7BR%7D%2C+v+%3D+y+-+%5Chat%7By%7D%3B+%5Cfrac%7B1%7D%7Bn%7D+vv%5E%7BT%7D+%26+%5C%5C%0A%5Cfrac%7B%5Cpartial%7B%7D%7D%7B%5Cpartial%7B%7D%5Chat%7By%7D%7D+%5Cleft%28+%5Cfrac%7B1%7D%7Bn%7D+vv%5E%7BT%7D+%5Cright%29+%26%3D+%5Cfrac%7B1%7D%7Bn%7D+%5Cleft%28+%5Cfrac%7B%5Cpartial%7B%7D%7D%7B%5Cpartial%7B%7D%5Chat%7By%7D%7D+%5Cleft%28+vv%5E%7BT%7D+%5Cright%29+%5Cright%29+%5C%5C%0A%26%3D+-%5Cfrac%7B1%7D%7Bn%7D+2v+%5Cequiv%7B%7D+-%5Cfrac%7B1%7D%7Bn%7D2%28y+-+%5Chat%7By%7D%29+%5C%5C%0A%5Cend%7Balign%2A%7D">

<!--
\text{A minor explanation on the vector derivative, } vv^{T} \text{is equivalent to } v^{2} \text{where the derivative of } v \text{via the chain rule is applied}
-->
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Ctext%7BA+minor+explanation+on+the+vector+derivative%2C+%7D+vv%5E%7BT%7D+%5Ctext%7Bis+equivalent+to+%7D+v%5E%7B2%7D+%5Ctext%7Bwhere+the+derivative+of+%7D+v+%5Ctext%7Bvia+the+chain+rule+is+applied%7D">

### Resources
- https://en.wikipedia.org/wiki/Mean_squared_error
- https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf

## Negative Log Likelihood

### Gradient Calculation

## Cross Entropy Loss

### Gradient Calculation
