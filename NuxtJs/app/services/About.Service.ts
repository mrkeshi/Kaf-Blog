import { Fetch } from "../utilities/CutsomMyFetchApi";
import { type ApiResponse } from "~/models/ApiRespose";
import {  type AboutDTO } from "~/models/About/AboutDTO";

export const getAboutMe = (): Promise<ApiResponse<AboutDTO>> => {
    return Fetch('/about',{
        method:'GET'
    });
}
