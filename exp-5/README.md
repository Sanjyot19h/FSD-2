 ## Optimize Frontend Performance using Lazy Loading

=Lazy Loading (React.lazy()) loads components only when they are needed, which helps reduce the initial bundle size and makes the app load faster.


=It uses dynamic imports, so the component code is fetched only when it gets rendered.


=Suspense with Fallback UI is used to wrap lazy-loaded components.


=The fallback prop shows a temporary UI (like "Loading...") while the component is being loaded, ensuring a smooth user experience.