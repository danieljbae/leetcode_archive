class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            # if op is number, add to record list
            if op.isnumeric():
                record.append(int(op))
            
            # negative number 
            elif op[0] == "-" and op[1:].isnumeric():
                record.append(int(op[1:]) * -1)

            # Add 2 previous scores and append to list
            elif op == "+":
                num1 = record[-1]
                num2 = record[-2]
                record.append(num1 + num2)
            
            # Remove most recent score
            elif op == "C":
                record.pop()
            
            # double most recent score
            elif op == "D":
                record.append(record[-1] * 2)
        
        return sum(record)