import { z } from 'zod';
import { format } from 'date-fns';

const validateNIKanddate_of_birth = (nik: string, date_of_birth: Date) => {
  const date_of_birthString = format(date_of_birth, 'ddMMyy');
  return nik.slice(6, 12) === date_of_birthString;
};

export const FormSchema = z.object({
  name: z
    .string()
    .min(2, {
      message: 'Username must be at least 2 characters.',
    })
    .regex(/^[a-zA-Z\s]*$/, {
      message: 'Name must only contain letters and spaces.',
    }),
  date_of_birth: z.date({ required_error: 'A date of birth is required' }),
  email: z.string().email(),
  identity_number: z
    .string()
    .length(16, { message: 'Identity number must be 16 digits' })
    .regex(/^\d+$/, { message: 'Identity number must be numerical' }),
}).refine((data) => {
  return validateNIKanddate_of_birth(data.identity_number, data.date_of_birth);
}, {
  message: 'Date of birth is not valid with Identity Number',
  path: ['date_of_birth'],
});
