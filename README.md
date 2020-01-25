# Another Book on Data Science - learn R and Python in parallel


This is a short book about data science and quantitative analysis, using R and Python together. The current version of the book has seven chapters.

## Chapters

#### 1. Introduction to R/Python Programming

R and Python are the two most popular programming languages used in data science. In this chapter, we go through the basics of R and Python programming in parallel with examples. Specifically, the topics of this chapter include variable, type, function, control flow, data structures, and object-oriented programming. The chapter is designed for both beginners and intermediate audience.

#### 2. More on R/Python Programming

Following the first chapter, the topics of this chapter include debugging, vectorization, parallelism, working with C++ in R/Python, and functional programming. These topics are chosen to help the audience to get familiar with some intermediate/advanced topics in R/Python programming. Mastering these topics will greatly help with coding skills. Like the first chapter, in this chapter, I try to emphasize the differences between R and Python with coding examples.

#### 3. data.table and pandas

In the first two chapters, we focus on general-purpose programming techniques. In this chapter, we introduce the very basics of data science, i.e., data manipulation. For the audience with little experience in data science, we start from a brief introduction to SQL. The major part of this chapter focuses on the two widely used data.frame packages, i.e., data.table in R and pandas in Python. Side-by-side examples using the two packages not only enables the audience to learn basic usages of these tools but also can be used as a quick reference manual.

#### 4. Random Variables & Distributions

In this chapter, we focus on statistics, which is the foundation of data science. To better follow this chapter, I recommend any introductory level statistics course as a prerequisite. The topics of this chapter include random variable sampling methods, distribution fitting, joint distribution/copula simulation, confidence interval calculation, and hypothesis testing.


#### 5. Linear Regression

This is a short but important chapter. In this chapter, we talk about linear regression models from scratch. Many textbooks introduce the theories behind linear regressions but still don’t help much on the implementation. We will see how the linear regression is implemented as a toy example in both R and Python with the help of linear algebra. I will also show how the basic linear regression model can be used for L2 penalized linear regression, i.e., ridge regression.


#### 6. Optimization in Practice

Most machine learning models rely on optimization algorithms. In this chapter, we give a brief introduction to optimization. Specifically, we will talk about convexity, gradient descent, general-purpose optimization tools in R and Python, linear programming and metaheuristic algorithms, etc. Based on these techniques, we will see coding examples about maximum likelihood estimation, linear regression, logistic regression, portfolio construction, traveling salesman problem.


#### 7. Machine Learning – A gentle introduction

Machine learning is a huge topic. In this chapter, I try to give a very short and gentle introduction to machine learning. It starts with a brief introduction of supervised learning, unsupervised learning and reinforcement learning, respectively. For supervised learning, we will see the gradient boosting regression with a pure Python implementation from scratch, from which the audience could learn the translation from the mathematical models to object-oriented programs. For unsupervised learning, the finite Gaussian mixture model and PCA are discussed. And for reinforcement learning, we will also use a simple game as an example to show the usage of deep Q-networks. The goal of this chapter is two-fold. First, I would like to give the audience an impression of what machine learning looks like. Second, reading the code snippets in this chapter could help the audience review/recap the topics in previous chapters.


### Read online

The book is now available on https://www.anotherbookondatascience.com/

And also a short link www.randpython.com


### FAQ

**Q:** How to report errors?

**A:** I appreciate it if you want to report errors found in the book. Please either email me setseed2016@gmail.com or open a github issue.

**Q:** More chapters to come?

**A:** Maybe in the future.

**Q:** Why is `dplyr` not covered?

**A:** I want to make the book concise with diversified topics about data science. Since `data.table` is introduced for data manipulation in the book, `dplyr` is not covered. `dplyr` is a great tool in R and there are many good learning resources.

