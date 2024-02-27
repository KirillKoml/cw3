import funcs.func
from clases.clases_oper import Operation

sort_list = funcs.func.last_executed_operation(funcs.func.list_date)

for i in sort_list:
    gg = Operation(i)
    print(gg.date())
    print(gg.from_to())
    print(f"""{gg.amount()}""")
