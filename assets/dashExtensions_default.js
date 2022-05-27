window.dashExtensions = Object.assign({}, window.dashExtensions, {
    default: {
        function0: (feature, context) => {
            console.log(context.pros, feature.properties.name)
            return context.includes(feature.properties.name)
        }

    }
});