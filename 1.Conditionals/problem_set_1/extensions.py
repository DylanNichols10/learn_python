def main():
    file = input("Please enter a file with extension: ")
    print(convert_file(file))

def convert_file(s):
    s = s.strip().lower()
    extension = s.split(".")[-1]
    match extension:
        case "gif":
            return ("image/gif")
        case "jpg" | "jpeg":
            return ("image/jpeg")
        case "png":
            return ("image/png")
        case "pdf":
            return ("application/pdf")
        case "txt":
            return ("text/plain")
        case "zip":
            return ("application/zip")
        case _:
            return ("application/octet-stream")
main()
