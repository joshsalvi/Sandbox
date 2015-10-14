import numpy as num


def pltsinx(nums):

    import numpy as num
    import matplotlib.pyplot as pypl

    pypl.plot(nums, num.sin(nums))
    pypl.show()

    print "First 10 elements of x: %s" % (str(nums[0:9]))
    print "First 10 elements of y: %s" % (str(num.sin(nums[0:9])))



pltsinx(num.linspace(0, 100, 100000))

