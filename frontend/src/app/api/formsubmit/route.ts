// pages/api/submitForm.ts
import type { NextApiRequest, NextApiResponse } from 'next';
import { NextResponse,NextRequest } from 'next/server'

import axios from 'axios';
import { env } from '@/lib/env.mjs';


// export async function POST() {   
//     return NextResponse.json({message:'method allow'})
//  }
export async function POST(req: NextRequest, res: NextResponse) {
    // console.log(req);
//   if (req.method === 'POST') {
    try {
        // console.log(req.body);
      const formData = await req.json();
      console.log(formData);
      // Example URL of another service where you want to send the data
      const apiUrl = env.BACKEND_ENDPOINT;

      // Example POST request using axios
      const response = await axios.post(apiUrl, formData);

      // Assuming response from the other service is returned to client
      return NextResponse.json({message:response.data},{status:200});
    } catch (error) {
    //   console.error('Error submitting form:', error);
    //   console.log(formData)
      return NextResponse.json({ error: 'Failed to submit form' },{status:500});
    }
//   } else {
//     res.setHeader('Allow', ['POST']);
//     res.status(405).end(`Method ${req.method} Not Allowed`);
//   }
}
 
// type ResponseData = {
//   message: string
// }
 
// export default function handler(
//   req: NextApiRequest,
//   res: NextApiResponse<ResponseData>
// ) {
//     console.log(req);
//   res.status(200).json({ message: 'Hello from Next.js!' })
// }