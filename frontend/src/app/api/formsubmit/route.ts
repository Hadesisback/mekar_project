import type { NextApiRequest, NextApiResponse } from 'next';
import { NextResponse,NextRequest } from 'next/server'
import axios from 'axios';
import { env } from '@/lib/env.mjs';



export async function POST(req: NextRequest, res: NextResponse) {
    try {
      const formData = await req.json();
      console.log(formData);
      const apiUrl = env.BACKEND_ENDPOINT;

      const response = await axios.post(apiUrl, formData);

      return NextResponse.json({message:response.data},{status:200});
    } catch (error) {
      console.error('Error submitting form:', error);
    //   console.log(formData)
      return NextResponse.json({ error: 'Failed to submit form', message:error},{status:500});
    }
  };
