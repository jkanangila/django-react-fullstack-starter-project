import React, { LazyExoticComponent, Suspense } from "react";
import ReactDOM from "react-dom";

let App = React.lazy(() => import("./App"));
let TodosIndexPage = React.lazy(() => import("./todos/pages/index.page"));

let declarePage = (id, Content) => {
  try {
    ReactDOM.render(
      <Suspense fallback={<></>}>
        <Content />
      </Suspense>,
      document.getElementById(id)
    );
  } catch {}
};

declarePage("app", App);
declarePage("todos-index", TodosIndexPage);
