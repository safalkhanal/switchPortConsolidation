def main():
    f = open("Archive/output/out.txt").read()
    s = open("Archive/output/source.txt").read()
    t = open("Archive/output/target.txt").read()
    print("Hi," + '\n' + "This email contaisns file with used port from source switch and unused port from target switch and source to target migration")
    if s == "":
        print('\n' + "No used port found in source switch" + '\n')
    if t == "":
        print('\n' + "No unused port found in target switch" + '\n')
    else:
        print("Please find the attached file(s) for more detailed output.")


if __name__ == '__main__':
    main()
