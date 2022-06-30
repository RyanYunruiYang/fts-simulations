# #Only used for generating animations. 
# def animate_func(num):  
#     ax.clear()  # Clears the figure to update the line, point, title, and axes  
#     # Updating Trajectory Line (num+1 due to Python indexing)
#     ax.plot3D(dataSet[0, :num+1], dataSet[1, :num+1], 
#               dataSet[2, :num+1], c='blue')
#     # Updating Point Location 
#     ax.scatter(dataSet[0, num], dataSet[1, num], dataSet[2, num], 
#                c='blue', marker='o')
#     # Adding Constant Origin
#     ax.plot3D(dataSet[0, 0], dataSet[1, 0], dataSet[2, 0],     
#                c='black', marker='o')
#     # Setting Axes Limits
#     ax.set_xlim3d([0, llink[0].maximum+1])
#     ax.set_ylim3d([0, llink[1].maximum+1])
#     ax.set_zlim3d([0, sim_length])
#     # Adding Figure Labels
#     ax.set_title('Trajectory \nIteration Number = ' + str(np.round(t[num],    
#                  decimals=2)) )#+ ' sec'
#     ax.set_xlabel('x')
#     ax.set_ylabel('y')
#     ax.set_zlabel('z')


        # # Determining Convergence
        # if(allmax and t>=llink[num_links-1].arrivaltime):
        #     nummax+=1
        # else:
        #     nummax = 0
        # if(allmax and nummax==100):
        #     print(str(maxcapacity)+" hits stability at: " + str(t-100))
        # if(t==sim_length-1 and nummax<100):
        #     print(str(maxcapacity)+" needs more than " + str(sim_length))

    # #Animation:
    # # Time Array
    # t = np.linspace(0, sim_length-1, sim_length)
    # # Position Arrays
    # x = np.asarray(linkSave[0])
    # y = np.asarray(linkSave[1])
    # z = np.linspace(0, 0, sim_length)
    # # z = np.linspace(0, sim_length-1, sim_length)
    # dataSet = np.array([x, y, z])  # Combining our position coordinates
    # numDataPoints = len(t)   

    # # Plotting the Animation
    # fig = plt.figure()
    # ax = plt.axes(projection='3d')
    # line_ani = animation.FuncAnimation(fig, animate_func, frames=numDataPoints)#interval=sim_length,
    # line_ani.save('animation.gif', writer='pillow')    
    # # plt.show()

    # # Colorscaled Static Plot
    # fig = plt.subplots()
    # plt.xlim(llink[0].minimum-1, llink[0].maximum+1)
    # plt.ylim(llink[1].minimum-1, llink[1].maximum+1)
    # plt.grid()
    # colors = np.array([100*i/sim_length for i in range(sim_length)])
    # plt.scatter(linkSave[0],linkSave[1],c=colors, cmap='viridis',s=10)
    # plt.show() # https://www.w3schools.com/python/matplotlib_scatter.asp