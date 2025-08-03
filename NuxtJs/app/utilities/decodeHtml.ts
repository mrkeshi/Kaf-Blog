const decodeHtml = (html: string): string => {
  const entityMap: Record<string, string> = {
    '&nbsp;': '\u00A0',
    '&lt;': '<',
    '&gt;': '>',
    '&amp;': '&',
    '&quot;': '"',
    '&#39;': "'",
    '&apos;': "'",
    '&zwnj;': '\u200C',
    '&zwj;': '\u200D',
    '&lrm;': '\u200E',
    '&rlm;': '\u200F',
    '&ndash;': '–',
    '&mdash;': '—',
    '&hellip;': '…',
    '&copy;': '©',
    '&reg;': '®',
    '&euro;': '€',
    '&trade;': '™',
    '&nbspi;': '\u00A0', // در صورتی که منظورت این باشه
  }

  return html.replace(/&[a-zA-Z0-9#]+;/g, match => {
    return entityMap[match] ?? match
  })
}
export default decodeHtml
