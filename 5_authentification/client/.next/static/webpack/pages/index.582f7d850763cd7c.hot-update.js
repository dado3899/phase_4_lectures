"use strict";
/*
 * ATTENTION: An "eval-source-map" devtool has been used.
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file with attached SourceMaps in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
self["webpackHotUpdate_N_E"]("pages/index",{

/***/ "./src/pages/index.js":
/*!****************************!*\
  !*** ./src/pages/index.js ***!
  \****************************/
/***/ (function(module, __webpack_exports__, __webpack_require__) {

eval(__webpack_require__.ts("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": function() { return /* binding */ Home; }\n/* harmony export */ });\n/* harmony import */ var react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react/jsx-dev-runtime */ \"./node_modules/react/jsx-dev-runtime.js\");\n/* harmony import */ var react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__);\n/* harmony import */ var next_head__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! next/head */ \"./node_modules/next/head.js\");\n/* harmony import */ var next_head__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(next_head__WEBPACK_IMPORTED_MODULE_1__);\n/* harmony import */ var next_image__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! next/image */ \"./node_modules/next/image.js\");\n/* harmony import */ var next_image__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(next_image__WEBPACK_IMPORTED_MODULE_2__);\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react */ \"./node_modules/react/index.js\");\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_3__);\n\nvar _s = $RefreshSig$();\n\n\n\n\n\nfunction Home() {\n    _s();\n    const [user, setUser] = (0,react__WEBPACK_IMPORTED_MODULE_3__.useState)(null);\n    const [username, setUsername] = (0,react__WEBPACK_IMPORTED_MODULE_3__.useState)(\"\");\n    (0,react__WEBPACK_IMPORTED_MODULE_3__.useEffect)(()=>{\n        console.log(\"Hello\");\n        fetch(\"/checklogin\").then((r)=>r.json()).then((user)=>setUser(user));\n    }, []);\n    function handleSubmit(e) {\n        e.preventDefault();\n        const data = {\n            \"name\": username\n        };\n        fetch(\"/login\", {\n            method: \"POST\",\n            headers: {\n                \"Content-Type\": \"application/json\"\n            },\n            body: JSON.stringify(data)\n        }).then((r)=>r.json()).then((user)=>setUser(user));\n    }\n    function handleLogout(e) {\n        e.preventDefault();\n        fetch(\"/logout\", {\n            method: \"DELETE\",\n            headers: {\n                \"Content-Type\": \"application/json\"\n            }\n        });\n    }\n    function checktype(e) {\n        e.preventDefault();\n        fetch(\"/get_type\").then((r)=>r.json()).then((data)=>console.log(data));\n    }\n    if (user) {\n        return /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.Fragment, {\n            children: [\n                /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"h2\", {\n                    children: [\n                        \"Welcome, \",\n                        user.name,\n                        \"!\"\n                    ]\n                }, void 0, true, {\n                    fileName: \"/Users/daviddoan/Documents/Phase-4/013023/Phase-4-Lectures/5_authentification/client/src/pages/index.js\",\n                    lineNumber: 54,\n                    columnNumber: 5\n                }, this),\n                /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"form\", {\n                    onSubmit: handleLogout,\n                    children: /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"button\", {\n                        type: \"submit\",\n                        children: \"Logout\"\n                    }, void 0, false, {\n                        fileName: \"/Users/daviddoan/Documents/Phase-4/013023/Phase-4-Lectures/5_authentification/client/src/pages/index.js\",\n                        lineNumber: 56,\n                        columnNumber: 9\n                    }, this)\n                }, void 0, false, {\n                    fileName: \"/Users/daviddoan/Documents/Phase-4/013023/Phase-4-Lectures/5_authentification/client/src/pages/index.js\",\n                    lineNumber: 55,\n                    columnNumber: 7\n                }, this),\n                /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"form\", {\n                    onSubmit: checktype,\n                    children: /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"button\", {\n                        type: \"submit\",\n                        children: \"checktype\"\n                    }, void 0, false, {\n                        fileName: \"/Users/daviddoan/Documents/Phase-4/013023/Phase-4-Lectures/5_authentification/client/src/pages/index.js\",\n                        lineNumber: 59,\n                        columnNumber: 9\n                    }, this)\n                }, void 0, false, {\n                    fileName: \"/Users/daviddoan/Documents/Phase-4/013023/Phase-4-Lectures/5_authentification/client/src/pages/index.js\",\n                    lineNumber: 58,\n                    columnNumber: 7\n                }, this)\n            ]\n        }, void 0, true);\n    } else {\n        return /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"form\", {\n            onSubmit: handleSubmit,\n            children: [\n                /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"input\", {\n                    type: \"text\",\n                    value: username,\n                    onChange: (e)=>setUsername(e.target.value)\n                }, void 0, false, {\n                    fileName: \"/Users/daviddoan/Documents/Phase-4/013023/Phase-4-Lectures/5_authentification/client/src/pages/index.js\",\n                    lineNumber: 66,\n                    columnNumber: 9\n                }, this),\n                /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"button\", {\n                    type: \"submit\",\n                    children: \"Login\"\n                }, void 0, false, {\n                    fileName: \"/Users/daviddoan/Documents/Phase-4/013023/Phase-4-Lectures/5_authentification/client/src/pages/index.js\",\n                    lineNumber: 71,\n                    columnNumber: 9\n                }, this)\n            ]\n        }, void 0, true, {\n            fileName: \"/Users/daviddoan/Documents/Phase-4/013023/Phase-4-Lectures/5_authentification/client/src/pages/index.js\",\n            lineNumber: 65,\n            columnNumber: 7\n        }, this);\n    }\n}\n_s(Home, \"JLuzdkPIN2RAZ1qjGhU9BQ+hy9c=\");\n_c = Home;\nvar _c;\n$RefreshReg$(_c, \"Home\");\n\n\n;\n    // Wrapped in an IIFE to avoid polluting the global scope\n    ;\n    (function () {\n        var _a, _b;\n        // Legacy CSS implementations will `eval` browser code in a Node.js context\n        // to extract CSS. For backwards compatibility, we need to check we're in a\n        // browser context before continuing.\n        if (typeof self !== 'undefined' &&\n            // AMP / No-JS mode does not inject these helpers:\n            '$RefreshHelpers$' in self) {\n            // @ts-ignore __webpack_module__ is global\n            var currentExports = module.exports;\n            // @ts-ignore __webpack_module__ is global\n            var prevExports = (_b = (_a = module.hot.data) === null || _a === void 0 ? void 0 : _a.prevExports) !== null && _b !== void 0 ? _b : null;\n            // This cannot happen in MainTemplate because the exports mismatch between\n            // templating and execution.\n            self.$RefreshHelpers$.registerExportsForReactRefresh(currentExports, module.id);\n            // A module can be accepted automatically based on its exports, e.g. when\n            // it is a Refresh Boundary.\n            if (self.$RefreshHelpers$.isReactRefreshBoundary(currentExports)) {\n                // Save the previous exports on update so we can compare the boundary\n                // signatures.\n                module.hot.dispose(function (data) {\n                    data.prevExports = currentExports;\n                });\n                // Unconditionally accept an update to this module, we'll check if it's\n                // still a Refresh Boundary later.\n                // @ts-ignore importMeta is replaced in the loader\n                module.hot.accept();\n                // This field is set when the previous version of this module was a\n                // Refresh Boundary, letting us know we need to check for invalidation or\n                // enqueue an update.\n                if (prevExports !== null) {\n                    // A boundary can become ineligible if its exports are incompatible\n                    // with the previous exports.\n                    //\n                    // For example, if you add/remove/change exports, we'll want to\n                    // re-execute the importing modules, and force those components to\n                    // re-render. Similarly, if you convert a class component to a\n                    // function, we want to invalidate the boundary.\n                    if (self.$RefreshHelpers$.shouldInvalidateReactRefreshBoundary(prevExports, currentExports)) {\n                        module.hot.invalidate();\n                    }\n                    else {\n                        self.$RefreshHelpers$.scheduleUpdate();\n                    }\n                }\n            }\n            else {\n                // Since we just executed the code for the module, it's possible that the\n                // new exports made it ineligible for being a boundary.\n                // We only care about the case when we were _previously_ a boundary,\n                // because we already accepted this update (accidental side effect).\n                var isNoLongerABoundary = prevExports !== null;\n                if (isNoLongerABoundary) {\n                    module.hot.invalidate();\n                }\n            }\n        }\n    })();\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvcGFnZXMvaW5kZXguanMuanMiLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7Ozs7QUFNTUE7QUFOc0I7QUFDRTtBQUVlO0FBQ0w7QUFJekIsU0FBU00sT0FBTzs7SUFDN0IsTUFBTSxDQUFDQyxNQUFNQyxRQUFRLEdBQUdILCtDQUFRQSxDQUFDLElBQUk7SUFDckMsTUFBTSxDQUFDSSxVQUFVQyxZQUFZLEdBQUdMLCtDQUFRQSxDQUFDO0lBQ3pDRCxnREFBU0EsQ0FBQyxJQUFJO1FBQ1pPLFFBQVFDLEdBQUcsQ0FBQztRQUNaQyxNQUFNLGVBQ0xDLElBQUksQ0FBQ0MsQ0FBQUEsSUFBS0EsRUFBRUMsSUFBSSxJQUNoQkYsSUFBSSxDQUFDUCxDQUFBQSxPQUFRQyxRQUFRRDtJQUN4QixHQUFFLEVBQUU7SUFDSixTQUFTVSxhQUFhQyxDQUFDLEVBQUU7UUFDdkJBLEVBQUVDLGNBQWM7UUFDaEIsTUFBTUMsT0FBTztZQUNYLFFBQVFYO1FBQ1Y7UUFFQUksTUFBTSxVQUFTO1lBQ1hRLFFBQVE7WUFDUkMsU0FBUztnQkFDUCxnQkFBZ0I7WUFDbEI7WUFDQUMsTUFBTUMsS0FBS0MsU0FBUyxDQUFDTDtRQUN2QixHQUNETixJQUFJLENBQUNDLENBQUFBLElBQUtBLEVBQUVDLElBQUksSUFDaEJGLElBQUksQ0FBQ1AsQ0FBQUEsT0FBTUMsUUFBUUQ7SUFDdEI7SUFFQSxTQUFTbUIsYUFBYVIsQ0FBQyxFQUFFO1FBQ3ZCQSxFQUFFQyxjQUFjO1FBQ2hCTixNQUFNLFdBQVU7WUFDZFEsUUFBUTtZQUNSQyxTQUFTO2dCQUNQLGdCQUFnQjtZQUNsQjtRQUNGO0lBQ0Y7SUFDQSxTQUFTSyxVQUFVVCxDQUFDLEVBQUU7UUFDcEJBLEVBQUVDLGNBQWM7UUFDaEJOLE1BQU0sYUFDTEMsSUFBSSxDQUFDQyxDQUFBQSxJQUFLQSxFQUFFQyxJQUFJLElBQ2hCRixJQUFJLENBQUNNLENBQUFBLE9BQVFULFFBQVFDLEdBQUcsQ0FBQ1E7SUFDNUI7SUFFQSxJQUFJYixNQUFNO1FBQ1IscUJBQ0E7OzhCQUNBLDhEQUFDcUI7O3dCQUFHO3dCQUFVckIsS0FBS3NCLElBQUk7d0JBQUM7Ozs7Ozs7OEJBQ3RCLDhEQUFDQztvQkFBS0MsVUFBVUw7OEJBQ2QsNEVBQUNNO3dCQUFPQyxNQUFLO2tDQUFTOzs7Ozs7Ozs7Ozs4QkFFeEIsOERBQUNIO29CQUFLQyxVQUFVSjs4QkFDZCw0RUFBQ0s7d0JBQU9DLE1BQUs7a0NBQVM7Ozs7Ozs7Ozs7Ozs7SUFJNUIsT0FBTztRQUNMLHFCQUNFLDhEQUFDSDtZQUFLQyxVQUFVZDs7OEJBQ2QsOERBQUNpQjtvQkFDQ0QsTUFBSztvQkFDTEUsT0FBTzFCO29CQUNQMkIsVUFBVSxDQUFDbEIsSUFBTVIsWUFBWVEsRUFBRW1CLE1BQU0sQ0FBQ0YsS0FBSzs7Ozs7OzhCQUU3Qyw4REFBQ0g7b0JBQU9DLE1BQUs7OEJBQVM7Ozs7Ozs7Ozs7OztJQUc1QixDQUFDO0FBQ0gsQ0FBQztHQWxFdUIzQjtLQUFBQSIsInNvdXJjZXMiOlsid2VicGFjazovL19OX0UvLi9zcmMvcGFnZXMvaW5kZXguanM/NDA4MCJdLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgSGVhZCBmcm9tICduZXh0L2hlYWQnXG5pbXBvcnQgSW1hZ2UgZnJvbSAnbmV4dC9pbWFnZSdcbmltcG9ydCB7IEludGVyIH0gZnJvbSAnbmV4dC9mb250L2dvb2dsZSdcbmltcG9ydCBzdHlsZXMgZnJvbSAnQC9zdHlsZXMvSG9tZS5tb2R1bGUuY3NzJ1xuaW1wb3J0IHt1c2VFZmZlY3QsdXNlU3RhdGV9IGZyb20gJ3JlYWN0J1xuXG5jb25zdCBpbnRlciA9IEludGVyKHsgc3Vic2V0czogWydsYXRpbiddIH0pXG5cbmV4cG9ydCBkZWZhdWx0IGZ1bmN0aW9uIEhvbWUoKSB7XG4gIGNvbnN0IFt1c2VyLCBzZXRVc2VyXSA9IHVzZVN0YXRlKG51bGwpO1xuICBjb25zdCBbdXNlcm5hbWUsIHNldFVzZXJuYW1lXSA9IHVzZVN0YXRlKFwiXCIpO1xuICB1c2VFZmZlY3QoKCk9PntcbiAgICBjb25zb2xlLmxvZyhcIkhlbGxvXCIpXG4gICAgZmV0Y2goJy9jaGVja2xvZ2luJylcbiAgICAudGhlbihyID0+IHIuanNvbigpKVxuICAgIC50aGVuKHVzZXIgPT4gc2V0VXNlcih1c2VyKSlcbiAgfSxbXSlcbiAgZnVuY3Rpb24gaGFuZGxlU3VibWl0KGUpIHtcbiAgICBlLnByZXZlbnREZWZhdWx0KCk7XG4gICAgY29uc3QgZGF0YSA9IHtcbiAgICAgIFwibmFtZVwiOiB1c2VybmFtZVxuICAgIH1cblxuICAgIGZldGNoKFwiL2xvZ2luXCIse1xuICAgICAgICBtZXRob2Q6IFwiUE9TVFwiLFxuICAgICAgICBoZWFkZXJzOiB7XG4gICAgICAgICAgXCJDb250ZW50LVR5cGVcIjogXCJhcHBsaWNhdGlvbi9qc29uXCIsXG4gICAgICAgIH0sXG4gICAgICAgIGJvZHk6IEpTT04uc3RyaW5naWZ5KGRhdGEpLFxuICAgICAgfSlcbiAgICAudGhlbihyID0+IHIuanNvbigpKVxuICAgIC50aGVuKHVzZXI9PnNldFVzZXIodXNlcikpXG4gIH1cbiAgXG4gIGZ1bmN0aW9uIGhhbmRsZUxvZ291dChlKSB7XG4gICAgZS5wcmV2ZW50RGVmYXVsdCgpO1xuICAgIGZldGNoKFwiL2xvZ291dFwiLHtcbiAgICAgIG1ldGhvZDogXCJERUxFVEVcIixcbiAgICAgIGhlYWRlcnM6IHtcbiAgICAgICAgXCJDb250ZW50LVR5cGVcIjogXCJhcHBsaWNhdGlvbi9qc29uXCIsXG4gICAgICB9LFxuICAgIH0pXG4gIH1cbiAgZnVuY3Rpb24gY2hlY2t0eXBlKGUpIHtcbiAgICBlLnByZXZlbnREZWZhdWx0KCk7XG4gICAgZmV0Y2goXCIvZ2V0X3R5cGVcIilcbiAgICAudGhlbihyID0+IHIuanNvbigpKVxuICAgIC50aGVuKGRhdGEgPT4gY29uc29sZS5sb2coZGF0YSkpXG4gIH1cblxuICBpZiAodXNlcikge1xuICAgIHJldHVybiAoXG4gICAgPD5cbiAgICA8aDI+V2VsY29tZSwge3VzZXIubmFtZX0hPC9oMj5cbiAgICAgIDxmb3JtIG9uU3VibWl0PXtoYW5kbGVMb2dvdXR9PlxuICAgICAgICA8YnV0dG9uIHR5cGU9XCJzdWJtaXRcIj5Mb2dvdXQ8L2J1dHRvbj5cbiAgICAgIDwvZm9ybT5cbiAgICAgIDxmb3JtIG9uU3VibWl0PXtjaGVja3R5cGV9PlxuICAgICAgICA8YnV0dG9uIHR5cGU9XCJzdWJtaXRcIj5jaGVja3R5cGU8L2J1dHRvbj5cbiAgICAgIDwvZm9ybT5cbiAgICA8Lz5cbiAgICApO1xuICB9IGVsc2Uge1xuICAgIHJldHVybiAoXG4gICAgICA8Zm9ybSBvblN1Ym1pdD17aGFuZGxlU3VibWl0fT5cbiAgICAgICAgPGlucHV0XG4gICAgICAgICAgdHlwZT1cInRleHRcIlxuICAgICAgICAgIHZhbHVlPXt1c2VybmFtZX1cbiAgICAgICAgICBvbkNoYW5nZT17KGUpID0+IHNldFVzZXJuYW1lKGUudGFyZ2V0LnZhbHVlKX1cbiAgICAgICAgLz5cbiAgICAgICAgPGJ1dHRvbiB0eXBlPVwic3VibWl0XCI+TG9naW48L2J1dHRvbj5cbiAgICAgIDwvZm9ybT5cbiAgICApXG4gIH1cbn1cbiJdLCJuYW1lcyI6WyJpbnRlciIsIkhlYWQiLCJJbWFnZSIsInN0eWxlcyIsInVzZUVmZmVjdCIsInVzZVN0YXRlIiwiSG9tZSIsInVzZXIiLCJzZXRVc2VyIiwidXNlcm5hbWUiLCJzZXRVc2VybmFtZSIsImNvbnNvbGUiLCJsb2ciLCJmZXRjaCIsInRoZW4iLCJyIiwianNvbiIsImhhbmRsZVN1Ym1pdCIsImUiLCJwcmV2ZW50RGVmYXVsdCIsImRhdGEiLCJtZXRob2QiLCJoZWFkZXJzIiwiYm9keSIsIkpTT04iLCJzdHJpbmdpZnkiLCJoYW5kbGVMb2dvdXQiLCJjaGVja3R5cGUiLCJoMiIsIm5hbWUiLCJmb3JtIiwib25TdWJtaXQiLCJidXR0b24iLCJ0eXBlIiwiaW5wdXQiLCJ2YWx1ZSIsIm9uQ2hhbmdlIiwidGFyZ2V0Il0sInNvdXJjZVJvb3QiOiIifQ==\n//# sourceURL=webpack-internal:///./src/pages/index.js\n"));

/***/ })

});