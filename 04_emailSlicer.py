def main():
    print("Welcome to the Email slicer.")
    print("")

    emailI = input("input your email address: ")

    (username, domain) = emailI.split("@")
    (domain, extension) = domain.split(".")

    print("Username: ", username)
    print("Domain: ",  domain)
    print("Extension: ", extension)

main()