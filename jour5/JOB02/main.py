def draw_rectangle(width, height):
    for larg in range(height):
        for long in range(width):
            if larg == 0 or long == height - 1:
                print('-', end='')
            elif larg == 0 or long == width - 1:
                print('|', end='')
            else:
                print(' ', end='')
        print()

# Example usage
draw_rectangle(10, 3)
