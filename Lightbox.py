# Krita Lightbox. Makes detailing/tracing layers easy.
# Put it in your Tools>Scripts>Ten Scripts for ease of use.
# Big thanks to tiar, KnowZero, freyalupen, LunarKreature and the great
# Krita-Artists.org-Community for helping me with my first script!
#
# If you use this script in a group layer, be sure to activate 
# pass-through" (symbols looks like a brickwall).

from krita import *
app = Krita.instance()
doc = app.activeDocument()

# topNode makes this all work in groups, too
current = doc.activeNode()
topNode = current.parentNode()

# setting up the information needed for the blue fill layer
infoFill = InfoObject()
infoFill.setProperty("color", "#0f87e6")
select = Selection()

# telling the application what region will be filled exactly, everything in this case
select.select(0, 0, doc.width(), doc.height(), 255)

# fill layer
fill = doc.createFillLayer("Non-Photo Blue", "color", infoFill, select)

# Take the current Painting Layers Opacity down to 50% before creating a new one
current_op = doc.activeNode().opacity()
if not doc.activeNode() == doc.nodeByName("Background"):
	doc.activeNode().setOpacity(current_op*0.5)
	doc.activeNode().setBlendingMode("multiply")
	
# Is there a 'Non-Photo Blue Layer'? If yes - delete before creating a new one
if doc.nodeByName("Non-Photo Blue"):
 	doc.nodeByName("Non-Photo Blue").remove()

# Add Non-Photo Blue Layer
topNode.addChildNode(fill, current)
layerBlueFill = doc.nodeByName("Non-Photo Blue")

layerBlueFill.setBlendingMode("screen")

paint = doc.createNode("Paint Layer", "paintlayer")
topNode.addChildNode(paint, None)

doc.refreshProjection()
