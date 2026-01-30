# default argument
def fun_param(studentname, age, fee=500):
    print(f"name{studentname},age:{age},fee:{fee}")


fun_param(studentname="sha", age=20)
fun_param(studentname="sn sn", age=10, fee=22555)
# agr hamm upr h fee k  value declare kr dete hai to niche print krate time
# upr wali print hoegi {fee=500}
# and agr ham niche value de dete hai to usko  h priority milegi
# fee=22555
