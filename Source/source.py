from PyPDF2 import PdfReader


class resume_analyzer:

    def extract_text(pdf):
        pdf_reader = PdfReader(pdf)

        # extrat text from each page separately
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        return text

    def resume_summary(text):
        prompt = f''' Summarize below data in 10 lines, use bullet points if required and finally conclude them.
                      {text}
                    '''
        return prompt

    def resume_strength(text):
        prompt = f''' Need to detailed analysis and explain the strengths of candidate in below resume.
                      {text}
                    '''
        return prompt

    def resume_weakness(text):
        prompt = f''' need to detailed analysis and explain of the weakness of below resume and how to improve make a better resume.
                      {text}
                    '''
        return prompt

    def job_title_suggestion(text):
        prompt = f''' What are the job roles i apply to linkedin based on below resume?. Suggest 8 job roles based on skills below.
                    {text}
                    '''
        return prompt

    def generate_response(google_api_key, llm,  task):

        output = llm.invoke(task)

        return output.content