def main():
    values = [12, 18, 21, 9, 31]
    total = sum(values)
    avg = total / len(values)
    print(f'Total: {total}')
    print(f'Average: {avg:.2f}')

if __name__ == '__main__':
    main()
