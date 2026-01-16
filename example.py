import sendspy

t = sendspy.token("token : ")
i = sendspy.id("id : ")
msg = "هلو "

sendspy.send(msg=msg, id=i, token=t)
