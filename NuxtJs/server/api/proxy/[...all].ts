import { defineEventHandler, readBody, getQuery, setResponseStatus } from 'h3';
import { $fetch } from 'ohmyfetch';

export default defineEventHandler(async (event) => {
  try {

    const fullUrl = event.req.url || '';
    const config=useRuntimeConfig()
 

    const proxyPrefix = '/api/proxy';
    let targetPath = '';
    if (fullUrl.startsWith(proxyPrefix)) {
      targetPath = fullUrl.slice(proxyPrefix.length);
    }

    const targetUrl = new URL(`${config.public.baseURL}${targetPath}`);

    const method = event.req.method.toUpperCase();

    let body = {};
    if (['POST', 'PUT', 'PATCH', 'DELETE'].includes(method)) {
      body = await readBody(event);
    }


    const headers = { ...event.req.headers,
      'Security-Token':config.private.private_header_key
     };
    delete headers.host;

    if (Object.keys(body).length && !headers['content-type']) {
      headers['content-type'] = 'application/json';
    }

    const fetchOptions: any = {
      method,
      headers,
      body: Object.keys(body).length ? body : undefined,
    };

    if (process.env.NODE_ENV === 'production') {
      fetchOptions.credentials = 'include';
    }


    const response = await $fetch(targetUrl.toString(), fetchOptions);

    return response;

  } catch (error: any) {
    setResponseStatus(event, error?.statusCode || 500);
    return { error: error.message || 'Unknown error in proxy' };
  }
});
