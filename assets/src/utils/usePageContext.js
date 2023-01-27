import { useEffect } from "react";
import { useState } from "react";

export let usePageContext = () => {
  let [pageContext, setPageContext] = useState();

  useEffect(() => {
    let pageContext = document.getElementById("page-context").textContent;
    setPageContext(JSON.parse(pageContext));
  }, []);

  return pageContext;
};
