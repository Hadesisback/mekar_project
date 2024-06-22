import axios, { AxiosError } from 'axios';
import { toast } from "@/components/ui/use-toast";

interface data_raw{
    name: string;
    email: string;
    identity_number: string;
    date_of_birth: Date;
}

export async function submitForm(data:data_raw, formattedDate:string){
    try {
        const response = await axios.post("/api/formsubmit", {
          ...data,
          date_of_birth: formattedDate,
        }, {
          headers: {
            'Content-Type': 'application/json',
          },
        });
    
        toast({
          title: 'You submitted the following values:',
          description: (
            <pre className="mt-2 w-[340px] rounded-md bg-slate-950 p-4">
              <code className="text-white">{JSON.stringify({ ...data, date_of_birth: formattedDate }, null, 2)}</code>
            </pre>
          ),
        });
        console.log('Form submitted successfully:', response.data);
    
  } catch (error: AxiosError | any) {
    if (error.response) {
      console.error('Error response status:', error.response.status);
      console.error('Error response data:', error.response.data);

    } else if (error.request) {
      console.error('Request made but no response received:', error.request);
 
    } else {
      console.error('Error setting up the request:', error.message);

    }

    console.error('Error submitting form:', error);
  }
};