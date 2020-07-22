# BASIC-Compiler
2020 PPCA BASIC Compiler Project

## 项目要求

完成一个basic语言的简易编译器。

#### ACM班（四周）：

完成一个从basic到AST到RISC-V机器码的编译器，包括检测出语法错误。

#### 工科（两周）：

完成一个basic到RISC-V机器码的编译器，不需要检测语法错误，不需要考虑内存的溢出问题。

#### 正确性测试：

生成的RISC-V机器码读入到自己写的simulator中，并输出return值。

HINT：INPUT操作可以使用命令行操作直接读入到一个寄存器中，然后存到对应的栈上。

*整个项目不允许使用外部的解析器，例如antlr。一经发现，扣除全部前端分数。



## BASIC语法规则

以下的解释包括了测试点中的所有语法。

基本语句形式：line number + statement

### 顺序语句

- `REM`：注释
- `LET var = expr`：普通赋值语句。
- `INPUT var1，var2`：读入一个数字存到变量中。
- `EXIT expr`：标志程序结束，停止执行，返回值为expr的值。当程序执行完最大的行号，也会自动停止执行，返回值为0。

### 控制语句

- `GOTO n`：直接跳转到第n条指令并执行。
- `IF exp THEN n`：cmp 包括>,< 以及==和!=；如果比较结果为真，则跳转到第n行，否则，继续按顺序执行到下一行。
- `FOR statement；exp cmp exp`：for循环的开始语句。`statement`是一个循环结束后执行的语句，`exp cmp exp`如果结果为假则跳出循环，执行`END FOR`的后一句。限制`statement`只能是`var = expr`的赋值语句。
- `END FOR`: for循环结束标识符，跳回for循环的起点。
- 注意：在每一个FOR中，GOTO的目标行号只在[FOR,ENDFOR]之间，如果跳到FOR句或ENDFOR句，则与“continue”同意义。

### 表达式形式

- atom expr：const_int 以及 `variable`。
- `expr op expr`：op包括+,-,*,/,&&,||,!=, ==, <, >, >=, <=。
- `(expr)`：将一个表达式用括号包裹，将改变计算的优先级。

#### 注意

BASIC语言是区分大小写的；

关键字不能被作为标识符（即变量名）；

变量名只由字母构成；

### ACM班额外语法

- `LET var = INT[N]`：数组生成语句，数组长度固定为N，生成后不得更改。
- 调用数组时，使用下标的形式，即`var[i]=expr` 或 `var2 = var[i]`。
- 高维数组以此类推。

### Reference

https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/index.html

《编译原理》（龙书）

## 评分标准   

90%正确性，10% report/code review



## Q&A

- Q: 乘除法怎么实现？ 

  A：修改simulator，加上两种乘除法语句。

- Q: BASIC语言有哪些数据类型？ 

  A：只有int类型，除非在IF的条件语句中会出现bool，但也只需要用简单的0/1的int。另外，除法结果为整数相除向下取整，和C++中的整数除法一致。

- Q：关键字包括什么？

  A：仅包含我们basic语言里的关键字，REM，IF，THEN，EXIT等等，其他语言无关。

- Q：优先级是什么？

  A：运算符优先级和C++一致。

- 所有的语句编号是从小到大的，但不一定连续。

- 不考虑变量的作用域，LET语句和INPUT语句即为引入变量/修改变量值。只要之前执行的语句有该变量，该变量即存在。在整个程序结束后才会销毁变量。