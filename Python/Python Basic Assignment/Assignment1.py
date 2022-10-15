#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''1. In the below elements which of them are values or an expression? eg:- values can be
integer or string and expressions will be mathematical operators.
*
'hello';
-87.8
-
/
+
6'''

Ans:
There are a total of 4 Operators and 3 Expressions, They are:
Operators: *,-,/,+
Expressions: 'hello', 87.8, 6


# In[ ]:


#2. What is the difference between string and variable?
Ans: 
    A Variable is used to store of information, and a String is a type of information you would store in a Variable. 
    A String is a group of characters or a single character usually enclosed in Double quotes " " or single quotes ' '


# In[11]:


#3. Describe three different data types.
# int data type
num=25
print(num, type(num))
# float data type
num=1.85
print(num, type(num))
# Complex data type
num= 5+8j
print(num, type(num))


# In[ ]:


#4. What is an expression made up of? What do all expressions do?

An expression is a combination of values, variables, operators.
If we ask Python to print an expression, the interpreter evaluates the expression and displays the result.


# In[7]:


4*5+20-40 # Is an Expression, The Python Interpreter Evaluates it to 0


# In[ ]:


#5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?

Ans: An expression is a combination of values, variables, and operators.
    When we type an expression at the prompt, the interpreter evaluates it, 
    which means that it finds the value of the expression.

eg: 4*5+20-40 is an example of a statement

A statement is a unit of code that has an effect, like creating a variable 
or displaying a value.When we type a statement, the interpreter executes it, 
which means that it does whatever the statement says. In general, statements don’t have values.

eg: variable declaration and assignment are statements because they do not return a value


# In[8]:


4*5+20-40 # Is a Expression
courseName = 'INeuron FullStack DataScience' # Is a Statement
print("Hello World !") # Is a Expression Statement


# In[ ]:


''''6. After running the following code, what does the variable bacon contain?
bacon = 22
bacon + 1'''

#Ans 
    The variable bacon is set to 22 .The expression bacon + 1 does not 
    reassign the value in bacon (that would the case if the expression is like bacon = bacon + 1 instead of bacon + 1)


# In[10]:


# Example Case#1
bacon=22
bacon+1
print(bacon)


# In[9]:


bacon=22
bacon=bacon+1 
print(bacon)


# In[ ]:





# In[6]:


'''7. What should the values of the following two terms be?
'spam'; + 'spamspam';
spam * 3'''
#Ans
print('spam' + 'spamspam') # concate
print('spam' * 3)    #multiply


# In[ ]:


#8. Why is eggs a valid variable name while 100 is invalid?
ANS:
1.varaible name should start with alphabets
2.The variable name should noyt contain any special characters like % $ ^ ! @ #
3.varaibles names can containnumber but you can't start with number.
4.Its a not strict rule you should start names with capital letter But it recommend to use small letters fror variables


# In[12]:


egg='Hello'
100='Python' 
print(egg) 
print(100)


# In[ ]:


#9. What three functions can be used to get the integer, floating-point number, or string version of a value?

 The int(),float(),and str() functions will evaluate to the integer,floating-point number,
    string version of the value passed to them.


# In[13]:


int(15.52)


# In[14]:


float(18)


# In[15]:


str(122)


# In[ ]:


get_ipython().set_next_input('10.Why does this expression cause an error? how can you fix it');get_ipython().run_line_magic('pinfo', 'it')
'I have eaten ' + 99 + 'burritos.'


# In[ ]:


ANS:
    since 99 is not string so need tp typecast to int to str


# In[17]:


'I have eaten ' + str(99) + ' burritos.'


# In[ ]:




