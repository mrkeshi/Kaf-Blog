import { Fetch } from "../utilities/CutsomMyFetchApi";
import { type ApiResponse } from "~/models/ApiRespose";
import {  type AboutDTO } from "~/models/About/AboutDTO";
import type { ContactDTO } from "~/models/Contact/ContactDTO";

export const sendContactDataService = (data:ContactDTO): Promise<ApiResponse<ContactDTO>> => {
 
    return Fetch<ContactDTO>('contact/',{
        method:'post',
        body:data
    });
}
