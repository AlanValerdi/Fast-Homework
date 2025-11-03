from docxtpl import DocxTemplate
import logging
import os

# Initialize logger
logger = logging.getLogger(__name__)

# Generate template path
template_Path = os.path.join(
    os.path.dirname(__file__),
    '../templates/template.docx'
)

# Output folder path
output_Path = os.path.join(
    os.path.dirname(__file__),
    "../output"
)


# Report generator func
def generate_report(data: dict, output_File_Name: str) -> str:
    
    try:
        # TODO: make both alumno and profesor request like
        # Change as the document 
        context = {
            "profesorVar": "Viktooorr",
            "alumno": "Alan Valerdi",
            "titulo": data.get("titulo", ""),
            "secciones": data.get("secciones", []),
            "bibliografia": data.get("bibliografia", [])
        }

        logger.info(f"Context being sent to template: {context}")

        # Upload temaplate
        doc = DocxTemplate(template_Path)
            
        doc.render(context)

        # Send output file
        output_file = os.path.join(output_Path, output_File_Name)        
        doc.save(output_file)

        return output_file
    except Exception as e:
        logger.error(f"Error in service/report_generator: {e}")
        raise


# Save to output folder



