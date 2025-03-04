define aoi = Character("Aoi")
# Aoi Expressions
image aoi normal = im.Scale("NormalAoi.png", 720, 920)
image aoi blushing = im.Scale("BlushingAoi.png", 720, 920) 
image aoi talking = im.Scale("TalkingAoi.png", 720, 920) 
image aoi crying = im.Scale("CryingAoi.png", 720, 920)

define kokoro = Character("Kokoro")
# Aoi Expressions
image kokoro normal = im.Scale("NormalKokoro.png", 520, 720)
image kokoro blushing = im.Scale("BlushingKokoro.png", 520, 720) 
image kokoro talking = im.Scale("TalkingKokoro.png", 520, 720) 
image kokoro excited = im.Scale("ExcitedKokoro.png", 520, 720) 
image kokoro sad = im.Scale("SadKokoro.png", 520, 720)

# background 
image bg house_up = im.Scale("bg house_up.png", 1920, 1080)
image bg park = im.Scale("bg park.webp", 1920, 1080)
image bg beach = im.Scale("bg beach.jpg", 1920, 1080)
image bg walk = im.Scale("bg walk.png", 1920, 1080)
image bg school = im.Scale("bg school.png", 1920, 1080)
image bg funeral = im.Scale("bg funeral.jpg", 1920, 1080)

label start:

    scene bg house_up
    show aoi normal at left
    show kokoro excited at center
    aoi "It's morning, and I walk up to Kokoro's front gate to pick her up for the park. She comes out and waves at me excitedly."
    jump scene2

label scene2:

    scene bg park
    show aoi talking at left
    show kokoro normal at center
    aoi "Kokoro and I walk to the local park, eating sandwiches she prepared. She looks at me for approval after I take a bite."
    menu:
        "It's good.":
            jump scene3_good
        "It's alright.":
            jump scene3_okay

label scene3_good:

    scene bg park
    show aoi normal at left
    show kokoro talking at center with dissolve 
    pause 1.5
    show kokoro excited at center
    kokoro "I'm glad you like it! I'll make some more next time!"
    jump scene4

label scene3_okay:

    scene bg park
    show aoi normal at left
    show kokoro sad at center with dissolve 
    pause 1.5
    show kokoro excited at center
    kokoro "Oh... I see. Well, let's enjoy the park!"
    jump scene4_alternate

label scene4:
    
    scene bg beach
    show aoi normal at left
    show kokoro normal at center
    aoi "Kokoro and I are sitting on the sand, looking towards the ocean. I look to my side and make eye contact with Kokoro."
    menu:
        "Confess.":
            jump scene5_confess
        "Blush and look away.":
            jump scene5_shy

label scene4_alternate:
    
    scene bg beach
    show aoi normal at left
    show kokoro normal at center
    aoi "Kokoro and I are sitting on the sand, looking towards the ocean. I look to my side and make eye contact with Kokoro."
    menu:
        "Confess.":
            jump scene5_alternate

label scene5_confess:
    
    scene bg beach
    show aoi blushing at left
    show kokoro blushing at center
    kokoro "I... I feel the same way!"
    aoi "Kokoro looks at me shyly and reciprocates the same feelings. We smile together and watch the horizon."
    jump scene6_next_day

label scene5_alternate:
    
    scene bg beach
    show aoi blushing at left
    show kokoro blushing at center
    aoi "Kokoro looks at me shyly. We smile together and watch the horizon anyway."
    jump scene6_awkward

label scene5_joke:
    
    scene bg beach
    show aoi blushing at left
    show kokoro talking at center
    kokoro "I don't think I feel the same way yet..."
    aoi "I get embarrsed and look away"


label scene5_shy:
    
    scene bg beach
    show aoi normal at left
    show kokoro blushing at center
    aoi "I notice Kokoro blush and looked away. I didn't pay much attention and I continue to look back to the ocean, I felt a nervous silence that filled the air. I noticed Kokoro's mood has changed."
    jump scene6_next_day_sad

label scene6_awkward:
    
    scene bg beach
    show aoi talking at left
    show kokoro blushing at center
    menu:
        "Tell her its a joke":
            jump scene5_shy
        "Play it off and talk about something else":
            jump scene6_alternate

label scene6_alternate:

    scene bg walk
    show aoi normal at left
    show kokoro blushing at center
    aoi "I notice Kokoro plays along but talks awkwardly. We head back to her house to drop her off and we exchange an awkward goodbye"
    jump scene7_next_day

label scene7_next_day:
    scene black  # Show a black screen

    show text "The Next Day" with fade

    pause 3.0  # Keep text on screen for 3 seconds

    jump scene7_awkward


label scene7_awkward:

    scene bg walk
    show aoi normal at center
    aoi "I walked up to Kokoro's front gate to pick her up on the way for school but she doesn't show up and I go ahead to school."
    jump awkward_ending

label awkward_ending:
    scene black  # Show a black screen

    pause 1.0  # Short pause before showing text

    show text "Thank you for playing.\nEnd of Part 1." with fade

    pause 3.0  # Keep text on screen for 3 seconds

    return  # Ends the game

label scene6_next_day:
    scene black  # Show a black screen

    show text "The Next Day" with fade

    pause 3.0  # Keep text on screen for 3 seconds

    jump scene6_happy

label scene6_happy:

    scene bg house_up
    show aoi normal at left
    show kokoro excited at center
    aoi "I walk to Kokoro's gate to pick her up for school, and she comes out the door with an excited smile."
    jump happy_ending

label happy_ending:
    scene black  # Show a black screen

    show text "Thank you for playing.\nEnd of Part 1." with fade

    pause 3.0  # Keep text on screen for 3 seconds

    return  # Ends the game

label scene6_next_day_sad:
    scene black  # Show a black screen

    show text "The Next Day" with fade
    
    pause 3.0  # Keep text on screen for 3 seconds

    jump scene6_sad

label scene6_sad:

    scene bg walk
    show aoi normal at left
    aoi "I walk to Kokoro’s gate to pick her up for school, but she doesn’t show up."
    menu:
        "Call her one more time.":
            show aoi talking at center
            jump scene7_worry
        "Go to school ahead.":
            jump scene7_normal

label scene7_worry:

    scene bg house_up
    show aoi crying at center
    aoi "Kokoro’s mom opens the door, eyes puffy and tired. 'Kokoro is in a coma... The probability of success isn’t high.'"
    jump scene8_tragic

label scene7_normal:

    scene bg school
    show aoi crying at center
    aoi "I spend most of the day at school and receive a call from Kokoro’s mom. She tells me that Kokoro never woke up. I rush to her house but get there too late."
    jump scene8_tragic

label scene8_tragic:

    scene bg funeral
    show aoi crying at center
    aoi "The funeral hall is filled with classmates and tears, excluding mine. I look at Kokoro’s casket and stay silent."
    jump tragic_ending

label tragic_ending:
    scene black  # Show a black screen

    show text "Thank you for playing.\nEnd of Part 1." with fade

    pause 3.0  # Keep text on screen for 3 seconds

    return  # Ends the game



