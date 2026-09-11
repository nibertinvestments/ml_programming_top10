def main():
    items = [12, 18, 21, 9, 31]
    total = sum(items)
    avg = total / len(items)
    print(f'Total: {total}')
    print(f'Average: {avg:.2f}')

if __name__ == '__main__':
    main()
