from fastapi import FastAPI
from reactpy import component,use_state,use_context,create_context,html
from reactpy.backend.fastapi import configure

my_ctx = create_context(None)

@component
def Myroot():
	# NOW CREATE CONTEXT 
	name,set_name = use_state("Test")
	return my_ctx(myparent(),value=[name,set_name])

# NOW I CREATE COMPONENT PARENT AND CHILD AND CHANGE VALUE NAME
# FROM CHILD COMPONENT

@component
def myparent():
	return html.div(
		{
			"style":{"background_color":"red",
				"color":"white","padding":"10px"
			}
		},
		html.h1("this is parent component"),
		child()
		)

# NOW CREATE CHILD COMPONET
@component
def child():
	# NOW CALL STATE NAME USE use_context
	name,set_name = use_context(my_ctx)

	return html.div(
		{
			"style":{"background_color":"blue",
				"color":"white","padding":"10px"
			}
		},
		html.h1("this is child component"),
		html.h1(name),
		# NOW I WILL CHANGE STATE myroot comonent from here
		html.input({
			"type":"text",
			"on_change":lambda event:set_name(event['target']['value'])
			}),
		

		)


app = FastAPI()
configure(app,Myroot)