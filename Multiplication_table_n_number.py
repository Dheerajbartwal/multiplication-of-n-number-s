        # this is a multiplication table of n number 




for i in range(2,20):
    with open(f"tables/of multiplication_{i} ", 'w') as f:
        for j in range(1,11):
            f.write(f"{i}X{j} = {i*j}")
            if j!=10:
                f.write('\n')



# crate a tables folder in your editor after run this this code automatic set multiplication table to given range 