import { updateDOM } from "@thi.ng/transducers-hdom"
import { sync } from "@thi.ng/rstream"


const main = sync<any, any>({}).transform(
    updateDOM()
);

if (process.env.NODE_ENV !== "production") {
    const hot = (<any>module).hot;
    hot && hot.dispose(() => main.done());
}