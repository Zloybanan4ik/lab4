monitor_cost = float(input("Enter the cost of a monitor: "))
system_unit_cost = float(input("Enter the cost of a system unit: "))
keyboard_cost = float(input("Enter the cost of a keyboard: "))
mouse_cost = float(input("Enter the cost of a mouse: "))

single_computer_cost = monitor_cost + system_unit_cost + keyboard_cost + mouse_cost

cost_for_three_computers = single_computer_cost * 3

n_computers = int(input("Enter the number of computers (N): "))

cost_for_n_computers = single_computer_cost * n_computers

print(f"The cost of 3 computers is: {cost_for_three_computers:.2f}")
print(f"The cost of {n_computers} computers is: {cost_for_n_computers:.2f}")
