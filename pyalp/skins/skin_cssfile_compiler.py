# from django.template.context import Context
# from django.template.loader import get_template_from_string

# from pyalp.skin import skin

# from pipeline.compilers import CompilerBase

# import pudb
# pu.db


# class SkinCSSFileCompiler(CompilerBase):
#     output_extension = 'css'

#     def match_file(self, filename):
#         import pudb
#         pu.db
#         return (
#             filename.endswith('.css.template') or
#             filename.endswith('.css.php')
#         )

#     def compile_file(self, infile, outfile, outdated=False, force=False):
#         if not outdated and not force:
#             return  # No need to recompiled file

#         with open(infile) as fh:
#             data = fh.read()

#         template = get_template_from_string(data, origin=infile)

#         context = Context({'skin': skin})
#         data = template.render(context)

#         with open(outfile, 'w') as fh:
#             fh.write(data)
