# No help() on method
# Instead:
# - write without parantheses

# command:
# > db.employees.find
# < [Function: find] AsyncFunction {
#   returnsPromise: true,
#   apiVersions: [ 1, Infinity ],
#   returnType: 'Cursor',
#   serverVersions: [ '0.0.0', '999.999.999' ],
#   topologies: [ 'ReplSet', 'Sharded', 'LoadBalanced', 'Standalone' ],
#   deprecated: false,
#   platforms: [ 'Compass', 'Browser', 'CLI' ],
#   isDirectShellCommand: false,
#   acceptsRawInput: false,
#   shellCommandCompleter: undefined,
#   newShellCommandCompleter: undefined,
#   help: [Function (anonymous)] Help
# }
# office>



'''
Q1. How do you get help for a specific method like `find()`?
Ans. Type the method name without parentheses to see its usage.
'''
# Example
# db.users.find
# → shows how the function is defined and used
