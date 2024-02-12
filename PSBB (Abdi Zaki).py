def calculate_min_buses(n, family_members):
    total_passengers = sum(family_members)
    if n != len(family_members):
        return "Input must be equal with count of family"
    min_buses = total_passengers // 4
    if total_passengers % 4 != 0:
        min_buses += 1
    return min_buses

# Input
n = int(input("Input the number of families : "))
family_members = list(map(int, input("Input the number of members in the family (separated by a space) : ").split()))

# Output
result = calculate_min_buses(n, family_members)
print("Minimum bus required is :", result)
