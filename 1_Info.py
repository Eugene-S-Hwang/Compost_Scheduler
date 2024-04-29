import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

image = Image.open("Food_Waste.webp")
st.image(image, caption="Every year, the world produces about 1.3 billion tons of food waste.")

st.write("""Every year, the world wastes about 1.3 billion tons of food, which is equivalent to 1/3 of all food produced and is worth about US$1 trillion. Food waste is a major contributor to climate change, 
         as it produces methane gas, which is 25 times more potent than carbon dioxide. In fact, if food waste were a country, it would be the third largest emitter of greenhouse gases, 
         behind the United States and China. In addition, food waste is a major contributor to world hunger. Annual food waste from just developed countries equate the entire net production of food in
         sub-Saharan Africa. This is why it is so important to reduce food waste, and composting is a great way to do so.""")

st.subheader("""What is composting and why should we do it?""")
st.write(""". Composting is a process where organic material, such as food waste, breaks down into a soil-like material 
         named compost that is rich in nutrients and can be used as fertilizer. """)
st.write("""There are numerous benefits for composting. Not only would it reduce the amount of food waste but it would also restores topsoil in places with poor soil quality and helps
         retain moisture in soil. In addition, composting reduces the need for chemical fertilizers, which are harmful to the environment, since compost naturally produces the necessary
         nutrients for plants to grow.
         Finally, if all food waste was composted, it would reduce global greenhouse emissions by up to 10%.""")
st.write("""Some may think that composting can only be done in facilities but in reality, it can easily be done by anyone at home. This app helps users manage their compost bin from start 
         to finish through a system of notifications and reminders. It also provides users with information on how to compost and how to use their compost.""")
st.subheader("""What do you put into a compost bin?""")
st.write("""There are four major components in create composts. The first component is browns, which should take up at least 2/3 of the total materials, are carbon-rich materials that provide energy for decomposing 
        the food waste. Examples of browns include dead leaves, branches, twigs, wood chips, paper, and cardboard.""")
st.write("""Greens, which should take up the remaining 1/3 of the total materials, 
         are nitrogen-rich. Examples include fruit and vegetable scraps, coffee grounds, grass clippings, hair and fur, and even manure from chickens, goats, and cattle. Make sure that they are
         cut up into small pieces. In order to avoid pests and rodents, it is important to not put meat, fish, dairy products, or oils into the compost bin.""")
st.write("""The last two components are
         water and air. It is also important throughout the compost process that the compost receives sunlight.""")
st.write("""Do not worry if there are earthworms in the compost bin. These are beneficial creatures that actually speeds up the decomposing process! However, there is no need for adding
         additional earthworms into the compost bin as you will find them naturally if your compost bin is in a yard and has an open floor. """)
st.write("""Additional material that should not be put in your compost bin include: pet waste, produce stickers, glossy paper, treated wood, weeds with seeds, 
        diseased plants, herbicide-treated plants, compostable bags (they're not compostable for backyard composting), and cooked food.""")

st.subheader("""Steps to Composting""")
st.write("""1. **Choose a space for the compost bin.**""")
st.write("""\t If you have a yard, you should place your compost bin in an area that is accessible year-round, has good drainage, and is near a water source. Please avoid placing it
        near a fence.""")
st.write("""\t If you do not have a yard, you can still compost in an indoors compost bin! However, the procedures may be a little different and this app mostly focuses on backyard
         composting.""")
st.write("""2. **Add browns and greens to your compost bin.**""")
st.write("""As stated before, your materials should be cut up into small pieces. If you need to store your materials before adding them to your compost bin, you should store greens in a freezer
         while you could set aside an area in your backyard for a steady supply of twigs, dried leaves, and other brownss.""")
st.write("""You should start your pile with a four-to-six inch layer of browns so that it would absorb extra liquids and allow air to circulate at the base of the pile. Next, 
        add the greens and browns in a layered fashion. You should add at least two to three times the volume of brown to the volume of greens. If necessary, moisturize the pile with a little bit of water.""")
st.write("""3. **Maintain your compost bin.**""")
st.write("""You should turn your compost bin every week, although you can do it as often as every three to four days. This allows for the pile to get some fresh air 
         which would speed up the composting process.""")
st.write("""The compost bin should heat up, especially around the center, and reach temperatures up to 130 degrees to 160 degrees Fahrenheit. This is important as this would reduce the
        possibility of there being any pathogens or weed seeds in the compost. If your compost bin is not heating up, you should add more greens and turn it.""")
st.write("""The pile should also not be dry or wet. It should have the consistency of a sponge. If it is too dry, add water and turn it. If it is too wet, add more browns and turn it.""")
st.write("""4. **Harvest your compost.**""")
st.write("""When your compost pile is no longer heating up and you cannot see anymore food scraps in the bin, you should allow the compost to cure for about 4 weeks. You should take out the compost
        and move it into a separate area. When it is done, it should have shrunk to about one-third of its original size.""")
st.write("""Your cured compost should now look dark, loose, and crumbly and smell like fresh dirt. Almost all of your food waste should have been decomposed at this point. The last thing
        for you to do is to sift through the compost to separate the soil with hard material that hasn't decomposed. You can use the hard material to add in a new or active compost pile.""")
st.write("""5. **Use the compost!**""")
st.write("""You can now use the compost just like a normal fertilizer or soil in your garden or lawn!""")
st.write("""Composting is a great way to help the environment while feeling fulfilling and rewarding. We hope that through using this app, you develop an appreciation for not only
        composting but also for the environment!""")

st.video("https://www.youtube.com/watch?v=dq-TkB8zZsI&ab_channel=AndrewMillison")
st.caption("This video shows a compost farm in Vermont. See how others compost!")

st.write("""**Sources:**""")
st.write("""1. https://www.epa.gov/recycle/composting-home""")
st.write("""2. https://updates.panda.org/driven-to-waste-report""")
st.write("3. https://www.wfp.org/stories/5-facts-about-food-waste-and-hunger")
st.write("4. Eunhye Yang from Critical Learning Club: https://www.criticallearningclub.com/about-us")