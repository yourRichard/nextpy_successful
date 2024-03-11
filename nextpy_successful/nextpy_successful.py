import nextpy as xt


def index() -> xt.Component:
    return xt.box(
        xt.box(
            xt.box(
                xt.box(
                    xt.box(
                        xt.image(src="/successful.svg",class_name="w-6 h-6"),
                        xt.text("You are scheduled",class_name="text-slate-800 text-lg font-bold tracking-wide"),
                        class_name="flex gap-4 justify-center item-center"
                    ),
                    xt.text("A calendar invitation has been sent to your email address.",
                    class_name="text-slate-700 pt-4"
                    ),
                    xt.box(
                        xt.text("open invitation"),
                        xt.image(src="/external_link.svg",class_name="w-6 h-6"),
                        class_name="flex justify-center item-center text-center w-36 h-8 border border-slate-800 rounded-2xl text-sm pt-1 gap-1 hover:bg-slate-100 transition-colors mx-auto my-4 cursor-pointer"
                    ),
                    class_name="py-12 text-center"
                ),
            ),
            class_name="h-[90%] w-[80%] bg-white"
        ),
        class_name="w-full h-full py-10 flex px-auto bg-slate-100 justify-center item-center"
    )




app = xt.App()
app.add_page(index)
