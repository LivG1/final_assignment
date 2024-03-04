import tkinter as tk
from PIL import Image, ImageTk
from tkmacosx import Button
import pygame as pg
from tkinter import messagebox
from tkinter import ttk


# the code to create my gui window
root = tk.Tk()
# the title to my gui
root.title("Where are we?")
# the code to determine the size of my gui window
# choose my sizing to fit the format of a vertical phone display like my app
screen_width = 450
screen_height = 750
root.minsize(screen_width, screen_height)



# create a definition to clear the window for a new page
def clear_widgets():
    # this function will destroy any widgets created
    for i in root.winfo_children():
        i.destroy()


# create the definition to place an image on the gui window
def add_image(root, file_path, width, height):
    # specify the variable name that creates your gui window and the image file path
    # specify global variables
    global pic, f1

    # Create the frame for the first windows of the game
    f1 = tk.Frame(root)
    # read the image you want to use for the first fra,e
    img = Image.open(file_path)
    # resize the image - make sure this is the same size as the gui window
    img = img.resize((width, height), Image.LANCZOS)
    # add this code to view the image as the frame
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(f1, image=pic)
    # code to just place the image
    Lab.pack()
    f1.pack()


# create a string variable that will hold the value of the checkbox
favorite = tk.StringVar()

# define a function that will be called once the state of the checkbox changed
def add_favorite():
    tk.messagebox.showinfo(title='Info',
                        message=favorite.get())


# create a definition that will display the unfollow confirm
def unfollow_sign():
    tk.messagebox.showwarning("NOTICE", "You've successfully unfollowed this profile!")


# create a definition that will display the deletion confirm
def delete_sign():
    tk.messagebox.showwarning("NOTICE", "You've successfully deleted your profile!")


# create a definition that will display the contact request
def contact_request():
    tk.messagebox.showwarning("NOTICE", "We've received you information request and will get back to you as soon as we can.")



# create my personal profile page
def profile_page():

    # clear widgets in the case widgets have been created
    clear_widgets()

    # add the code which creates the design of the profile
    # change the background of the page
    root.configure(bg="Light Grey")

    # add the profile icon
    icon1 = tk.Label(root,
                     text="👤",
                     font="Arial 80 bold",
                     bg="Light Grey"
                     )
    icon1.place(x=187, y=91)


    # add white labels for the background design of the window
    p1 = tk.Label(root,
                  text="",
                  bg="White",
                  width=18,
                  height=3
                  )
    p1.place(x=147, y=186)

    p2 = tk.Label(root,
                  text="",
                  bg="White",
                  width=45,
                  height=4
                  )
    p2.place(x=20, y=272)

    p3 = tk.Label(root,
                  text="",
                  bg="White",
                  width=37,
                  height=15
                  )
    p3.place(x=56, y=366)

    p4 = tk.Label(root,
                  text="",
                  bg="White",
                  width=45,
                  height=2
                  )
    p4.place(x=20, y=636)

    p5 = tk.Label(root,
                  text="",
                  bg="White",
                  width=45,
                  height=2
                  )
    p5.place(x=20, y=696)

    # add an entry box where the user can enter the profile name
    name = tk.StringVar()
    name1 = tk.Entry(root,
                     textvar=name,
                     font="Arial 25 bold",
                     fg="Black",
                     bg="White",
                     width=10
                     )
    name1.place(x=154, y=192)

    # add the profile status
    status1 = tk.Label(root,
                       text="Status",
                       font="Arial 14",
                       fg="Black",
                       bg="White"
                       )
    status1.place(x=25, y=277)

    # add an entry box where the user can change his status
    status = tk.StringVar()
    status1_text = tk.Entry(root,
                            textvar=status,
                            font="Arial 18",
                            fg="Grey",
                            bg="White",
                            width=35
                            )
    status1_text.place(x=25, y=297)

    # add a settings label
    settings = tk.Label(root,
                        text="⚙️ Settings",
                        font="Arial 18",
                        fg="Black",
                        bg="White"
                        )
    settings.place(x=177, y= 382)

    # add an account label
    account = tk.Label(root,
                       text="🔑 Account",
                       font="Arial 18",
                       fg="Black",
                       bg="White"
                       )
    account.place(x=176, y=418)

    # add a privacy label
    privacy = tk.Label(root,
                       text="🔒 Privacy",
                       font="Arial 18",
                       fg="Black",
                       bg="White"
                       )
    privacy.place(x=178, y=454)

    # add an add friends label
    add_friends = tk.Label(root,
                        text="👥 Add friends",
                        font="Arial 18",
                        fg="Black",
                        bg="White"
                        )
    add_friends.place(x=163, y=490)

    # add an edit profile label
    add_friends = tk.Label(root,
                           text="🖊️ Edit Profile",
                           font="Arial 18",
                           fg="Black",
                           bg="White"
                           )
    add_friends.place(x=163, y=526)

    # add the share location option
    location1_text = tk.Label(root,
                              text="📍Share my location",
                              font="Arial 18",
                              fg="Black",
                              bg="White"
                              )
    location1_text.place(x=130, y=562)

    location1 = ttk.Checkbutton(root,
                                 text="",
                                 command=add_favorite,
                                 variable=favorite,
                                 onvalue='You are now sharing your location.',
                                 offvalue='You are no longer sharing your location.'
                                 )
    location1.place(x=305, y=566)

    # add a contact option
    contact = Button(root,
                    text="Contact & Questions",
                    font="Arial 18",
                    fg="Blue",
                    bg="White",
                    command=contact_request
                    )
    contact.place(x=125, y=640)

    # add a delete option
    delete = Button(root,
                       text="Delete your profile",
                       font="Arial 18",
                       fg="Red",
                       bg="White",
                       command=delete_sign
                       )
    delete.place(x=133, y=700)

    # add an exit button to reenter the homepage
    exit1 = Button(root,
                   text="< Exit",
                   font="Arial 16",
                   fg="Blue",
                   bg="White",
                   borderless=1,
                   command=homepage
                   )
    exit1.place(x=25, y=20)


# create the three profile pages for my friends
# first friend: Chrissi
def chrissi_page():

    # clear widgets in the case widgets have been created
    clear_widgets()

    # end the pg.mixer.music from the call_crissi page when hanging up
    pg.quit()

    # add the code which creates the design of the profile
    # change the background of the page
    root.configure(bg="Light Grey")

    # add the profile icon
    icon1 = tk.Label(root,
                     text="👩🏽‍💼",
                     font="Arial 80 bold",
                     bg="Light Grey"
                     )
    icon1.place(x=185, y=100)

    # add the profile name
    chrissi_name = tk.Label(root,
                            text="Chrissi",
                            font="Arial 25 bold",
                            fg="Black",
                            bg="Light grey"
                            )
    chrissi_name.place(x=182, y=200)


    # add white labels for the background design of the window
    c1 = tk.Label(root,
                  text="",
                  bg="White",
                  width=45,
                  height=3
                  )
    c1.place(x=20, y=281)

    c2 = tk.Label(root,
                  text="",
                  bg="White",
                  width=45,
                  height=5
                  )
    c2.place(x=20, y=356)

    c3 = tk.Label(root,
                  text="",
                  bg="White",
                  width=45,
                  height=9
                  )
    c3.place(x=20, y=464)

    c4 = tk.Label(root,
                  text="",
                  bg="White",
                  width=45,
                  height=2
                  )
    c4.place(x=20, y=636)

    c5 = tk.Label(root,
                  text="",
                  bg="White",
                  width=45,
                  height=2
                  )
    c5.place(x=20, y=696)


    # add the profile status
    status1 = tk.Label(root,
                       text="Status",
                       font="Arial 14",
                       fg="Black",
                       bg="White"
                       )
    status1.place(x=25, y=284)

    status1_text = tk.Label(root,
                            text="Currently at work",
                            font="Arial 18",
                            fg="Grey",
                            bg="White"
                            )
    status1_text.place(x=25, y= 304)

    # add the profile address
    address1 = tk.Label(root,
                        text="Home",
                        font="Arial 14",
                        fg="Black",
                        bg="White"
                        )
    address1.place(x=25, y=359)

    address1_text1 = tk.Label(root,
                             text="Lotentengasse 42",
                             font="Arial 18",
                             fg="Grey",
                             bg="White"
                             )
    address1_text1.place(x=25, y=381)

    address1_text2 = tk.Label(root,
                             text="22304 Hamburg",
                             font="Arial 18",
                             fg="Grey",
                             bg="White"
                             )
    address1_text2.place(x=25, y=407)

    # add the call option
    call1 = Button(root,
                   text="📞",
                   font="Arial 60 bold",
                   bg="White",
                   width=80,
                   command=call_chrissi
                   )
    call1.place(x=90, y=489)

    call1_text = tk.Label(root,
                          text="call contact",
                          font="Arial 14",
                          fg="Black",
                          bg="White",
                          )
    call1_text.place(x=92, y=574)

    # add the location option
    locate1 = Button(root,
                     text="📍",
                     font="Arial 60 bold",
                     bg="White",
                     width=80,
                     command=locate_chrissi
                     )
    locate1.place(x=283, y=489)

    locate1_text = tk.Label(root,
                          text="view location",
                          font="Arial 14",
                          fg="Black",
                          bg="White",
                          )
    locate1_text.place(x=281, y=574)

    # add the add to favorites option
    favorites1_text = tk.Label(root,
                              text="Add profile to favorites",
                              font="Arial 16",
                              fg="Blue",
                              bg="White"
                              )
    favorites1_text.place(x=25, y=642)

    favorites1 = ttk.Checkbutton(root,
                                 text="",
                                 command=add_favorite,
                                 variable=favorite,
                                 onvalue='Profile added to favorites!',
                                 offvalue='Profile removed from favorites!'
                                 )
    favorites1.place(x=180, y=645)

    # add an unfollow option
    unfollow1 = Button(root,
                       text="Unfollow this profile",
                       font="Arial 16",
                       fg="Red",
                       bg="White",
                       command=unfollow_sign
                       )
    unfollow1.place(x=140, y=700)

    # add an exit button to reenter the homepage
    exit1 = Button(root,
                   text="< Exit",
                   font="Arial 16",
                   fg="Blue",
                   bg="White",
                   borderless=1,
                   command=homepage
                   )
    exit1.place(x=25, y=20)


# second friend: Nadine
def nadine_page():

    # clear widgets in the case widgets have been created
    clear_widgets()

    # end the pg.mixer.music from the call_nadine page when hanging up
    pg.quit()

    # add the code which creates the design of the profile
    # change the background of the page
    root.configure(bg="Light Grey")

    # add the profile icon
    icon1 = tk.Label(root,
                     text="👩🏻‍💼",
                     font="Arial 80 bold",
                     bg="Light Grey"
                     )
    icon1.place(x=185, y=100)

    # add the profile name
    nadine_name = tk.Label(root,
                            text="Nadine",
                            font="Arial 25 bold",
                            fg="Black",
                            bg="Light grey"
                            )
    nadine_name.place(x=185, y=200)


    # add white labels for the background design of the window
    n1 = tk.Label(root,
                  text="",
                  bg="White",
                  width=45,
                  height=3
                  )
    n1.place(x=20, y=281)

    n2 = tk.Label(root,
                  text="",
                  bg="White",
                  width=45,
                  height=5
                  )
    n2.place(x=20, y=356)

    n3 = tk.Label(root,
                  text="",
                  bg="White",
                  width=45,
                  height=9
                  )
    n3.place(x=20, y=464)

    n4 = tk.Label(root,
                  text="",
                  bg="White",
                  width=45,
                  height=2
                  )
    n4.place(x=20, y=636)

    n5 = tk.Label(root,
                  text="",
                  bg="White",
                  width=45,
                  height=2
                  )
    n5.place(x=20, y=696)


    # add the profile status
    status1 = tk.Label(root,
                       text="Status",
                       font="Arial 14",
                       fg="Black",
                       bg="White"
                       )
    status1.place(x=25, y=284)

    status1_text = tk.Label(root,
                            text="Live, Love, Laugh 💕",
                            font="Arial 18",
                            fg="Grey",
                            bg="White"
                            )
    status1_text.place(x=25, y= 304)

    # add the profile address
    address1 = tk.Label(root,
                        text="Home",
                        font="Arial 14",
                        fg="Black",
                        bg="White"
                        )
    address1.place(x=25, y=359)

    address1_text1 = tk.Label(root,
                             text="Tarrestraße 64",
                             font="Arial 18",
                             fg="Grey",
                             bg="White"
                             )
    address1_text1.place(x=25, y=381)

    address1_text2 = tk.Label(root,
                             text="22110 Hamburg",
                             font="Arial 18",
                             fg="Grey",
                             bg="White"
                             )
    address1_text2.place(x=25, y=407)

    # add the call option
    call1 = Button(root,
                   text="📞",
                   font="Arial 60 bold",
                   bg="White",
                   width=80,
                   command=call_nadine
                   )
    call1.place(x=90, y=489)

    call1_text = tk.Label(root,
                          text="call contact",
                          font="Arial 14",
                          fg="Black",
                          bg="White",
                          )
    call1_text.place(x=92, y=574)

    # add the location option
    locate1 = Button(root,
                     text="📍",
                     font="Arial 60 bold",
                     bg="White",
                     width=80,
                     command=locate_nadine
                     )
    locate1.place(x=283, y=489)

    locate1_text = tk.Label(root,
                          text="view location",
                          font="Arial 14",
                          fg="Black",
                          bg="White",
                          )
    locate1_text.place(x=281, y=574)

    # add the add to favorites option
    favorites1_text = tk.Label(root,
                              text="Add profile to favorites",
                              font="Arial 16",
                              fg="Blue",
                              bg="White"
                              )
    favorites1_text.place(x=25, y=642)

    favorites1 = ttk.Checkbutton(root,
                                 text="",
                                 command=add_favorite,
                                 variable=favorite,
                                 onvalue='Profile added to favorites!',
                                 offvalue='Profile removed from favorites!'
                                 )
    favorites1.place(x=180, y=645)

    # add an unfollow option
    unfollow1 = Button(root,
                       text="Unfollow this profile",
                       font="Arial 16",
                       fg="Red",
                       bg="White",
                       command=unfollow_sign
                       )
    unfollow1.place(x=140, y=700)

    # add an exit button to reenter the homepage
    exit1 = Button(root,
                   text="< Exit",
                   font="Arial 16",
                   fg="Blue",
                   bg="White",
                   borderless=1,
                   command=homepage
                   )
    exit1.place(x=25, y=20)


# third friend: Francesca
def francesca_page():

    # clear widgets in the case widgets have been created
    clear_widgets()

    # end the pg.mixer.music from the call_francesca page when hanging up
    pg.quit()

    # add the code which creates the design of the profile
    # change the background of the page
    root.configure(bg="Light Grey")

    # add the profile icon
    icon1 = tk.Label(root,
                     text="👩🏼‍💼",
                     font="Arial 80 bold",
                     bg="Light Grey"
                     )
    icon1.place(x=185, y=100)

    # add the profile name
    francesca_name = tk.Label(root,
                            text="Francesca",
                            font="Arial 25 bold",
                            fg="Black",
                            bg="Light grey"
                            )
    francesca_name.place(x=165, y=200)


    # add white labels for the background design of the window
    f1 = tk.Label(root,
                  text="",
                  bg="White",
                  width=45,
                  height=3
                  )
    f1.place(x=20, y=281)

    f2 = tk.Label(root,
                  text="",
                  bg="White",
                  width=45,
                  height=5
                  )
    f2.place(x=20, y=356)

    f3 = tk.Label(root,
                  text="",
                  bg="White",
                  width=45,
                  height=9
                  )
    f3.place(x=20, y=464)

    f4 = tk.Label(root,
                  text="",
                  bg="White",
                  width=45,
                  height=2
                  )
    f4.place(x=20, y=636)

    f5 = tk.Label(root,
                  text="",
                  bg="White",
                  width=45,
                  height=2
                  )
    f5.place(x=20, y=696)


    # add the profile status
    status1 = tk.Label(root,
                       text="Status",
                       font="Arial 14",
                       fg="Black",
                       bg="White"
                       )
    status1.place(x=25, y=284)

    status1_text = tk.Label(root,
                            text="The grind never stops!",
                            font="Arial 18",
                            fg="Grey",
                            bg="White"
                            )
    status1_text.place(x=25, y= 304)

    # add the profile address
    address1 = tk.Label(root,
                        text="Home",
                        font="Arial 14",
                        fg="Black",
                        bg="White"
                        )
    address1.place(x=25, y=359)

    address1_text1 = tk.Label(root,
                             text="Hansusweg 1",
                             font="Arial 18",
                             fg="Grey",
                             bg="White"
                             )
    address1_text1.place(x=25, y=381)

    address1_text2 = tk.Label(root,
                             text="22291 Hamburg",
                             font="Arial 18",
                             fg="Grey",
                             bg="White"
                             )
    address1_text2.place(x=25, y=407)

    # add the call option
    call1 = Button(root,
                   text="📞",
                   font="Arial 60 bold",
                   bg="White",
                   width=80,
                   command=call_francesca
                   )
    call1.place(x=90, y=489)

    call1_text = tk.Label(root,
                          text="call contact",
                          font="Arial 14",
                          fg="Black",
                          bg="White",
                          )
    call1_text.place(x=92, y=574)

    # add the location option
    locate1 = Button(root,
                     text="📍",
                     font="Arial 60 bold",
                     bg="White",
                     width=80,
                     command=locate_francesca
                     )
    locate1.place(x=283, y=489)

    locate1_text = tk.Label(root,
                          text="view location",
                          font="Arial 14",
                          fg="Black",
                          bg="White",
                          )
    locate1_text.place(x=281, y=574)

    # add the add to favorites option
    favorites1_text = tk.Label(root,
                              text="Add profile to favorites",
                              font="Arial 16",
                              fg="Blue",
                              bg="White"
                              )
    favorites1_text.place(x=25, y=642)

    favorites1 = ttk.Checkbutton(root,
                                 text="",
                                 command=add_favorite,
                                 variable=favorite,
                                 onvalue='Profile added to favorites!',
                                 offvalue='Profile removed from favorites!'
                                 )
    favorites1.place(x=180, y=645)

    # add an unfollow option
    unfollow1 = Button(root,
                       text="Unfollow this profile",
                       font="Arial 16",
                       fg="Red",
                       bg="White",
                       command=unfollow_sign
                       )
    unfollow1.place(x=140, y=700)

    # add an exit button to reenter the homepage
    exit1 = Button(root,
                   text="< Exit",
                   font="Arial 16",
                   fg="Blue",
                   bg="White",
                   borderless=1,
                   command=homepage
                   )
    exit1.place(x=25, y=20)



# create the three pages to call each friend
# first friend: Chrissi
def call_chrissi():

    # clear widgets in the case widgets have been created
    clear_widgets()

    # add the code which creates the design of the call
    # change the background of the page to simulate a call
    root.configure(bg="Black")

    # initialize the pygame library
    pg.init()

    # load calling music
    pg.mixer.music.load("music/call.mp3")
    pg.mixer.music.play(0)

    # add a calling label
    calling_label = tk.Label(root,
                             text="calling Chrissi...",
                             font="Arial 30",
                             fg="White",
                             bg="Black"
                             )
    calling_label.place(x=120, y=150)

    # add the call structure
    symbols1 = tk.Label(root,
                        text="🔇     📱     🔊",
                        font="Arial 40 bold",
                        bg="Black"
                        )
    symbols1.place(x=108, y=300)

    # add the designations to the symbols
    labels1 = tk.Label(root,
                       text=" mute               keypad            audio",
                       font="Arial 15",
                       bg="Black",
                       fg="Grey"
                       )
    labels1.place(x=103, y=360)

    # add the second row of the call structure
    symbols2 = tk.Label(root,
                        text="💬     📹     👤",
                        font="Arial 40 bold",
                        bg="Black"
                        )
    symbols2.place(x=108, y=400)

    # add the designations to the second row of symbols
    labels2 = tk.Label(root,
                       text="add call          FaceTime         contacts",
                       font="Arial 15",
                       bg="Black",
                       fg="Grey"
                       )
    labels2.place(x=100, y=460)

    # add a button to end the call
    decline_button = Button(root,
                            text="📞",
                            font="Arial 40 bold",
                            fg="White",
                            bg="Red",
                            borderless=1,
                            width=60,
                            command=chrissi_page
                            )
    decline_button.place(x=195, y=585)


# second friend: Nadine
def call_nadine():

    # clear widgets in the case widgets have been created
    clear_widgets()

    # add the code which creates the design of the call
    # change the background of the page to simulate a call
    root.configure(bg="Black")

    # initialize the pygame library
    pg.init()

    # load calling music
    pg.mixer.music.load("music/call.mp3")
    pg.mixer.music.play(0)

    # add a calling label
    calling_label = tk.Label(root,
                             text="calling Nadine...",
                             font="Arial 30",
                             fg="White",
                             bg="Black"
                             )
    calling_label.place(x=120, y=150)

    # add the call structure
    symbols1 = tk.Label(root,
                        text="🔇     📱     🔊",
                        font="Arial 40 bold",
                        bg="Black"
                        )
    symbols1.place(x=108, y=300)

    # add the designations to the symbols
    labels1 = tk.Label(root,
                       text=" mute               keypad            audio",
                       font="Arial 15",
                       bg="Black",
                       fg="Grey"
                       )
    labels1.place(x=103, y=360)

    # add the second row of the call structure
    symbols2 = tk.Label(root,
                        text="💬     📹     👤",
                        font="Arial 40 bold",
                        bg="Black"
                        )
    symbols2.place(x=108, y=400)

    # add the designations to the second row of symbols
    labels2 = tk.Label(root,
                       text="add call          FaceTime         contacts",
                       font="Arial 15",
                       bg="Black",
                       fg="Grey"
                       )
    labels2.place(x=100, y=460)

    # add a button to end the call
    decline_button = Button(root,
                            text="📞",
                            font="Arial 40 bold",
                            fg="White",
                            bg="Red",
                            borderless=1,
                            width=60,
                            command=nadine_page
                            )
    decline_button.place(x=195, y=585)


# third friend: Francesca
def call_francesca():

    # clear widgets in the case widgets have been created
    clear_widgets()

    # add the code which creates the design of the call
    # change the background of the page to simulate a call
    root.configure(bg="Black")

    # initialize the pygame library
    pg.init()

    # load calling music
    pg.mixer.music.load("music/call.mp3")
    pg.mixer.music.play(0)

    # add a calling label
    calling_label = tk.Label(root,
                             text="calling Francesca...",
                             font="Arial 30",
                             fg="White",
                             bg="Black"
                             )
    calling_label.place(x=100, y=150)

    # add the call structure
    symbols1 = tk.Label(root,
                        text="🔇     📱     🔊",
                        font="Arial 40 bold",
                        bg="Black"
                        )
    symbols1.place(x=108, y=300)

    # add the designations to the symbols
    labels1 = tk.Label(root,
                       text=" mute               keypad            audio",
                       font="Arial 15",
                       bg="Black",
                       fg="Grey"
                       )
    labels1.place(x=103, y=360)

    # add the second row of the call structure
    symbols2 = tk.Label(root,
                        text="💬     📹     👤",
                        font="Arial 40 bold",
                        bg="Black"
                        )
    symbols2.place(x=108, y=400)

    # add the designations to the second row of symbols
    labels2 = tk.Label(root,
                       text="add call          FaceTime         contacts",
                       font="Arial 15",
                       bg="Black",
                       fg="Grey"
                       )
    labels2.place(x=100, y=460)

    # add a button to end the call
    decline_button = Button(root,
                            text="📞",
                            font="Arial 40 bold",
                            fg="White",
                            bg="Red",
                            borderless=1,
                            width=60,
                            command=francesca_page
                            )
    decline_button.place(x=195, y=585)



# create the three pages to locate each friend
# first friend: Chrissi
def locate_chrissi():

    # add the code which creates the design of the locator map
    # initialize our pygame library
    pg.init()

    # determine the size of the window: same size to imitate a phone screen
    size = width, height = 450, 750
    # determine the background image of the page
    bg = pg.image.load("images/map1.jpg")
    # determine the speed of the runner
    speed = [1, 1]  # higher numbers make the runner go faster

    # create the screen
    screen = pg.display.set_mode(size)

    # set a caption for the window
    pg.display.set_caption("Where is Chrissi?")

    # the code for the image of the runner
    chrissi = pg.image.load("images/Chrissi.png")
    chrissi_rect = chrissi.get_rect()

    # create a button to close the location page
    # create a font for the button text
    font = pg.font.SysFont('arial', 16)

    # create a surface for the button
    button_surface = pg.Surface((100, 22))

    # change the color and border of the button
    pg.draw.rect(button_surface, (255, 255, 255), (1, 1, 99, 21))
    pg.draw.rect(button_surface, (0, 0, 0), (1, 1, 99, 21), 1)

    # render the text on the button
    text = font.render("< Exit", True, (0, 0, 255))
    text_rect = text.get_rect(center=(button_surface.get_width() / 2, button_surface.get_height() / 2))

    # create a pg.Rect to determine the button's boundaries and position
    button_rect = pg.Rect(25, 20, 100, 22)

    # the code for closing the window or pressing the button
    while True:
        for event in pg.event.get():
            # close the page when clicked on the windows red button
            if event.type == pg.QUIT:
                pg.quit()
                chrissi_page()
            # close the page when clicked on the created exit button
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                # call the on_mouse_button_down() function
                if button_rect.collidepoint(event.pos):
                    pg.quit()
                    chrissi_page()


        # the code to move the runner symbolising my friend
        chrissi_rect = chrissi_rect.move(speed)

        # if else statement to reverse the speed when it reaches the boundaries
        if chrissi_rect.left < 0 or chrissi_rect.right > width:
            speed[0] = -speed[0]
        if chrissi_rect.top < 0 or chrissi_rect.bottom > height:
            speed[1] = -speed[1]

        # the code to change the background to an image
        # without this the image overlays the moving image of the runner
        screen.blit(bg, (0, 0))
        # the code to show the button text
        button_surface.blit(text, text_rect)
        # the code to draw the button on the screen
        screen.blit(button_surface, (button_rect.x, button_rect.y))
        # the code to place the image on the display
        screen.blit(chrissi, chrissi_rect)
        # the code to launch the location page
        pg.display.update()


# second friend: Nadine
def locate_nadine():

    # add the code which creates the design of the locator map
    # initialize our pygame library
    pg.init()

    # determine the size of the window: same size to imitate a phone screen
    size = width, height = 450, 750
    # determine the background image of the page
    bg = pg.image.load("images/map2.jpg")
    # determine the speed of the runner
    speed = [1, 1]  # higher numbers make the runner go faster

    # create the screen
    screen = pg.display.set_mode(size)

    # set a caption for the window
    pg.display.set_caption("Where is Nadine?")

    # the code for the image of the runner
    nadine = pg.image.load("images/Nadine.png")
    nadine_rect = nadine.get_rect()

    # create a button to close the location page
    # create a font for the button text
    font = pg.font.SysFont('arial', 16)

    # create a surface for the button
    button_surface = pg.Surface((100, 22))

    # change the color and border of the button
    pg.draw.rect(button_surface, (255, 255, 255), (1, 1, 99, 21))
    pg.draw.rect(button_surface, (0, 0, 0), (1, 1, 99, 21), 1)

    # render the text on the button
    text = font.render("< Exit", True, (0, 0, 255))
    text_rect = text.get_rect(center=(button_surface.get_width() / 2, button_surface.get_height() / 2))

    # create a pg.Rect to determine the button's boundaries and position
    button_rect = pg.Rect(25, 20, 100, 22)


    # the code for closing the window or pressing the button
    while True:
        for event in pg.event.get():
            # close the page when clicked on the windows red button
            if event.type == pg.QUIT:
                pg.quit()
                nadine_page()
            # close the page when clicked on the created exit button
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                # Call the on_mouse_button_down() function
                if button_rect.collidepoint(event.pos):
                    pg.quit()
                    nadine_page()


        # the code to move the runner symbolising my friend
        nadine_rect = nadine_rect.move(speed)

        # if else statement to reverse the speed when it reaches the boundaries
        if nadine_rect.left < 0 or nadine_rect.right > width:
            speed[0] = -speed[0]
        if nadine_rect.top < 0 or nadine_rect.bottom > height:
            speed[1] = -speed[1]

        # the code to change the background to an image
        # without this the image overlays the moving image
        screen.blit(bg, (0, 0))
        # the code to show the button text
        button_surface.blit(text, text_rect)
        # the code to draw the button on the screen
        screen.blit(button_surface, (button_rect.x, button_rect.y))
        # the code to place the image on the display
        screen.blit(nadine, nadine_rect)
        # the code to launch the location page
        pg.display.update()


# third friend: Francesca
def locate_francesca():

    # add the code which creates the design of the locator map
    # initialize our pygame library
    pg.init()

    # determine the size of the window: same size to imitate a phone screen
    size = width, height = 450, 750
    # determine the background image of the page
    bg = pg.image.load("images/map3.jpg")
    # determine the speed of the runner
    speed = [1, 1]  # higher numbers make the runner go faster

    # create the screen
    screen = pg.display.set_mode(size)

    # set a caption for the window
    pg.display.set_caption("Where is Francesca?")

    # the code for the image of the runner
    francesca = pg.image.load("images/Francesca.png")
    francesca_rect = francesca.get_rect()

    # create a button to close the location page
    # create a font for the button text
    font = pg.font.SysFont('arial', 16)

    # create a surface for the button
    button_surface = pg.Surface((100, 22))

    # change the color and border of the button
    pg.draw.rect(button_surface, (255, 255, 255), (1, 1, 99, 21))
    pg.draw.rect(button_surface, (0, 0, 0), (1, 1, 99, 21), 1)

    # render the text on the button
    text = font.render("< Exit", True, (0, 0, 255))
    text_rect = text.get_rect(center=(button_surface.get_width() / 2, button_surface.get_height() / 2))

    # create a pg.Rect to determine the button's boundaries and position
    button_rect = pg.Rect(25, 20, 100, 22)

    # the code for closing the window or pressing the button
    while True:
        for event in pg.event.get():
            # close the page when clicked on the windows red button
            if event.type == pg.QUIT:
                pg.quit()
                #quit()
                francesca_page()
            # close the page when clicked on the created exit button
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                # Call the on_mouse_button_down() function
                if button_rect.collidepoint(event.pos):
                    pg.quit()
                    francesca_page()

        # the code to move the runner symbolising my friend
        francesca_rect = francesca_rect.move(speed)

        # if else statement to reverse the speed when it reaches the boundaries
        if francesca_rect.left < 0 or francesca_rect.right > width:
            speed[0] = -speed[0]
        if francesca_rect.top < 0 or francesca_rect.bottom > height:
            speed[1] = -speed[1]

        # the code to change the background to an image
        # without this the image overlays the moving image
        screen.blit(bg, (0, 0))
        # the code to show the button text
        button_surface.blit(text, text_rect)
        # the code to draw the button on the screen
        screen.blit(button_surface, (button_rect.x, button_rect.y))
        # the code to place the image on the display
        screen.blit(francesca, francesca_rect)
        # the code to launch the location page
        pg.display.update()


# create the homepage of my app
def homepage():

    # clear widgets in the case widgets have been created
    clear_widgets()

    # add the code which creates the design of my homepage window
    # create the home page background
    add_image(root, "images/map.jpeg", screen_width, screen_height)

    # create a header for the locations to find on the map
    locate_label = tk.Label(root,
                             text="Locate your Friends..",
                             relief=tk.RIDGE,
                             font="arial 24 bold",
                             bg="White",
                             fg="Grey",
                             borderwidth="5"
                             )
    locate_label.place(x=85, y=20)

    # add buttons with names of the three women representing their location
    Chrissi = Button(root,
                     text="Chrissi",
                     relief="raised",
                     font="arial 15 bold",
                     bg="Light Pink",
                     fg="Black",
                     borderwidth="4",
                     command=chrissi_page
                     )
    Chrissi.place(x=300, y=150)

    Nadine = Button(root,
                    text="Nadine",
                    relief="raised",
                    font="arial 15 bold",
                    bg="Light Blue",
                    fg="Black",
                    borderwidth="4",
                    command=nadine_page
                    )
    Nadine.place(x=100, y=250)

    Francesca = Button(root,
                       text="Francesca",
                       relief="raised",
                       font="Arial 15 bold",
                       bg="Light Yellow",
                       fg="Black",
                       borderwidth="4",
                       command=francesca_page
                       )
    Francesca.place(x=200, y=450)

    # add a label to simulate a white border
    border = tk.Label(root,
                      text="",
                      bg="White",
                      width=50,
                      height=8
                      )
    border.place(x=0, y=640)

    # add a profile label
    profile_label = tk.Label(root,
                             text="Profile",
                             font="Arial 15 bold",
                             fg="Grey",
                             bg="White"
                             )
    profile_label.place(x=299, y=712)

    # add a button to access your profile
    profile = Button(root,
                     text="👤",
                     #relief="groove",
                     font="Arial 30 bold",
                     bg="White",
                     #borderwidth="5",
                     width=50,
                     command=profile_page
                     )
    profile.place(x=300, y=665)

    # add a friends label
    call_emergency_label = tk.Label(root,
                             text="Emergency",
                             font="Arial 15 bold",
                             fg="Grey",
                             bg="White"
                             )
    call_emergency_label.place(x=89, y=712)

    # add a button to access your profile
    call_emergency = Button(root,
                     text="☎️",
                     font="Arial 30 bold",
                     bg="White",
                     width=50,
                     command=call_page
                     )
    call_emergency.place(x=105, y=665)


# create the emergency call page
def call_page():

    # clear widgets in the case widgets have been created
    clear_widgets()

    # add the code which creates the design of my emergency call window
    # change the background of the page to simulate a call
    root.configure(bg="Black")

    # initialize the pygame library
    pg.init()

    # load calling music
    pg.mixer.music.load("music/911.mp3")
    pg.mixer.music.play(0)

    # add a calling label
    calling_label = tk.Label(root,
                             text="calling...",
                             font="Arial 30",
                             fg="White",
                             bg="Black"
                             )
    calling_label.place(x=168, y=150)

    # add the call structure
    symbols1 = tk.Label(root,
                        text="🔇     📱     🔊",
                        font="Arial 40 bold",
                        bg="Black"
                        )
    symbols1.place(x=108, y=300)

    # add the designations to the symbols
    labels1 = tk.Label(root,
                       text=" mute               keypad            audio",
                       font="Arial 15",
                       bg="Black",
                       fg="Grey"
                       )
    labels1.place(x=103, y=360)

    # add the second row of the call structure
    symbols2 = tk.Label(root,
                        text="💬     📹     👤",
                        font="Arial 40 bold",
                        bg="Black"
                        )
    symbols2.place(x=108, y=400)

    # add the designations to the second row of symbols
    labels2 = tk.Label(root,
                       text="add call          FaceTime         contacts",
                       font="Arial 15",
                       bg="Black",
                       fg="Grey"
                       )
    labels2.place(x=100, y=460)

    # add a button to end the call
    decline_button = Button(root,
                            text="📞",
                            font="Arial 40 bold",
                            fg="White",
                            bg="Red",
                            borderless=1,
                            width=60,
                            command=safety_page
                            )
    decline_button.place(x=195, y=585)


# create the initial safety page of my app that appears upon launching
def safety_page():

    # clear widgets in the case widgets have been created
    clear_widgets()

    # end the pg.mixer.music from the emergency call_page when hanging up
    pg.quit()

    # add the code which creates the design of my first window
    # change the background of the page
    root.configure(bg="Light Grey")

    # add the emergency label
    emergency_label = tk.Label(root,
                             text="EMERGENCY!",
                             font="Arial 40 bold",
                             fg="White",
                             bg="Red"
                             )
    emergency_label.place(x=87, y=100)

    # add a label for further text
    danger_label = tk.Label(root,
                            text="Are you in danger?",
                            font="Arial 30 bold",
                            fg="Red",
                            bg="White"
                            )
    danger_label.place(x=86, y=160)

    # add a label to symbolize a call
    phone_label = tk.Label(root,
                           text="☎️",
                           font="Arial 60 bold",
                           bg="Light Grey"
                           )
    phone_label.place(x=195, y=265)

    # add an emergency call button
    call_button = Button(root,
                         text="HELP",
                         font="Arial 40 bold",
                         fg="Red",
                         bg="White",
                         bordercolor="Red",
                         command=call_page
                         )
    call_button.place(x=135, y=350)

    # add the call instructions label
    call_label = tk.Label(root,
                          text="Call for help!",
                          font="Arial 25 bold",
                          fg="Red",
                          bg="Light Grey",
                          )
    call_label.place(x=145, y=440)

    # add the homepage instructions label
    enter_label = tk.Label(root,
                           text="Proceed to Homepage",
                           font="Arial 17 bold",
                           fg="Grey",
                           bg="Light Grey",
                           )
    enter_label.place(x=135, y=580)

    # add a homepage button
    homepage_button = Button(root,
                             text="🏠",
                             font="Arial 40 bold",
                             width=60,
                             borderless=1,
                             command=homepage
                             )
    homepage_button.place(x=195, y=615)


# call my homepage definition to create the home page when launching the gui
safety_page()


# the code to execute my code
root.mainloop()
