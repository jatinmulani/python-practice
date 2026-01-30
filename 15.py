#   variable lenth keywords argument ==> **kwargs
def fun_parm(**num):
    print(num)


fun_parm(a=10, b=10, name="jatin", class_type="python")
# output ==> {'a': 10, 'b': 10, 'name': 'jatin', 'class_type': 'python'}
fun_parm(gauttam="kumawta", z=10, high_level_order="difficult",)
# {'gauttam': 'kumawta', 'z': 10, 'high_level_order': 'difficult'}
