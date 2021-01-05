 Dynamic Scope

    The dynamic scope allocation rules are used for non-block structured languages
    By considering the current activation, it determines the scope of declaration of the names at runtime

Example: LISP and SNOBOL are the languages which use dynamic scope rule.

    In this type of scoping, the non-local variables access refers to the non-local data which is declared in most recently called and still active procedures
    Therefore, each time, new bindings are set up for local names called procedure
    Symbol tables are required at runtime in dynamic scoping
    The two ways to implement non-local accessing under dynamic scoping are:

Deep Access
Shallow Access

Deep Access:

    The idea is to keep a stack of active variables. Use control links instead of access links and to find a variable, search the stack from top to bottom looking for most recent activation record that contains the space for desired variables
    This method of accessing nonlocal variables is called deep access. Since search is made “deep” in the stack, hence the method is called deep access. In this method, a symbol table should be used at runtime

Shallow Access

    The idea to keep a central storage and allot one slot for every variable name
    If the names are not created at runtime then the storage layout can be fixed at compile time. Otherwise, when new activation procedure occurs, then that procedure changes the storage entries for its local at entry and exit (i.e., while entering in the procedure and while leaving the procedure)

Comparison of Deep and Shallow Access
Deep Access
It needs a symbol table at runtime

Shallow Access
Deep access takes longer time to access the nonlocals
	
Shallow access allows fast access	
It has a overhead of handling procedure entry and exit

810920
250968
