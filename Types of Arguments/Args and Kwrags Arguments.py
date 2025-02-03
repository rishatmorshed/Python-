def info_person(*args, **kwrags):  #Key Word argument works with dictionary and *args work with tuple
    for key, value in kwrags.items():
        print(key, value)
    print(args)

info_person(1,2, name = "Morshed", age = 30, dept = "cse")
info_person(1,2,3, name = "Mahbub", dept="cse")