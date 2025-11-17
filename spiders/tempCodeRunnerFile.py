 os.path.dirname(os.path.abspath(__file__))
    test_path = os.path.join(local_dir, "test.txt")
    with open(test_path, "w", encoding="utf-8") as f:
        f.write(soup.prettify()