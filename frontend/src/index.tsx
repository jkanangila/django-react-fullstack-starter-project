import React, { LazyExoticComponent, Suspense } from "react";
import ReactDOM from "react-dom";

const App = React.lazy(() => import("./App"));

const declarePage = (id: string, Content: LazyExoticComponent<any>) => {
  try {
    ReactDOM.render(
      <Suspense fallback={<></>}>
        <Content />
      </Suspense>,
      document.getElementById(id)
    );
  } catch (e) {
    // Do nothing
  }
};

declarePage("app", App);
