import nextpy as xt


def meeting_details(title):
    return xt.box(
        xt.box(
            xt.box(
                xt.text(title)
            ),
            class_name="w-[10rem] h-[10rem] border-slate-100"
        ),
    )