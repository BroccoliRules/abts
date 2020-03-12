from tethys_sdk.base import TethysAppBase, url_map_maker


class LoversAbts(TethysAppBase):
    """
    Tethys app class for Lovers Abts.
    """

    name = 'Lovers Abts'
    index = 'lovers_abts:home'
    icon = 'lovers_abts/images/icon.gif'
    package = 'lovers_abts'
    root_url = 'lovers-abts'
    color = '#d35400'
    description = ''
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='lovers-abts',
                controller='lovers_abts.controllers.home'
            ),
            
            
            UrlMap(
                 name='proposal',
                 url='lovers-abts/proposal',
                 controller='lovers_abts.controllers.proposal'
                   ),
        )

        return url_maps
