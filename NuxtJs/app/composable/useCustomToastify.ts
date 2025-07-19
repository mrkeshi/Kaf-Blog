

type ToastParams = {
  title: string
  message: string
  type?: 'success' | 'error' | 'info' | 'warning' | 'default'
  theme?: 'dark' | 'light' | 'colored' | 'auto'
  autoClose?: number | boolean
  toastId?: string
  icon?: string | false
  rtl?: boolean
  hideProgressBar?: boolean
}

export function useCustomToastify() {
  const showError = ({
    title,
    message,
    type = 'error',
    theme = 'dark',
    autoClose = 3000,
    toastId,
    icon,
    rtl = true,
    hideProgressBar = true,
  }: ToastParams) => {
    useToastify(`${title}<br>${message}`, {
      type,
      theme,
      toastId,
      autoClose,
      dangerouslyHTMLString: true,
      icon,
      rtl,
      hideProgressBar,
      
      toastClassName: 'custom-toast',
      bodyClassName: 'custom-toast-body',
    })
  }

  return { showError }
}
