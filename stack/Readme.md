# 스택

스택은 선입후출(First In Last Out) 형태의 자료구조이다
스택에 삽입하는 연산을 `push`, 꺼내는 연산을 `pop` 이라 한다

## 스택의 ADT

`ADT` (`abstract data type`) 은 추상 자료형을 말한다
추상 자료형은 이터페이스만 있고 실제로 구현은 되지 않은 자료형을 말한다

스택은 `push`, `pop`, `isFull`, `isEmpty`, `top` 와 같은 연산을 정의해야 한다

```ts
interface Stack<T> {
  push: (stack: [T], item: T) => void;
  pop: (stack: [T]) => T;
  isFull: () => boolean;
  isEmpty: () => boolean;
  top: int;
  data: [T];
}
```

## 스택 구현

```py
stack = []
max_size = 10
top = 0

def isFull(stack):
    return len(stack) == max_size

def isEmpty(stack):
    return len(stack) == 0

def pop(stack):
    if isEmpty(stack):
        print('stack is empty')
    else:
        popItem = stack[len(stack) - 1]
        stack.pop()
        top -= 1
        return popItem

def push(stack, item):
    if (isFull(stack)):
        print('stack is full')
    else:
        stack.append(item)
        top += 1
```
